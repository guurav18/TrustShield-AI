"""
Utility functions for TrustShield AI Deepfake Detection System
Handles frame extraction, preprocessing, and data loading
"""

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

import numpy as np
import os
from pathlib import Path


# Lazy load face detector cascade
FACE_CASCADE = None

def get_face_cascade():
    global FACE_CASCADE
    if FACE_CASCADE is None and HAS_CV2:
        try:
            cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            FACE_CASCADE = cv2.CascadeClassifier(cascade_path)
        except Exception:
            FACE_CASCADE = None
    return FACE_CASCADE


def crop_face(frame, padding=0.2, target_size=(224, 224)):
    """
    Detect face in frame, add padding, crop, and resize to target_size.
    Falls back to center square crop if no face is detected.
    """
    if frame is None:
        return None
        
    h, w, _ = frame.shape
    cascade = get_face_cascade()
    
    if cascade is not None:
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(40, 40))
            
            if len(faces) > 0:
                # Find largest face by area
                largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
                fx, fy, fw, fh = largest_face
                
                # Add padding
                pad_w = int(fw * padding)
                pad_h = int(fh * padding)
                
                x1 = max(0, fx - pad_w)
                y1 = max(0, fy - pad_h)
                x2 = min(w, fx + fw + pad_w)
                y2 = min(h, fy + fh + pad_h)
                
                face_crop = frame[y1:y2, x1:x2]
                if face_crop.size > 0:
                    return cv2.resize(face_crop, (target_size[1], target_size[0]))
        except Exception:
            pass
            
    # Fallback: Center crop (square)
    min_dim = min(h, w)
    start_x = (w - min_dim) // 2
    start_y = (h - min_dim) // 2
    crop = frame[start_y:start_y + min_dim, start_x:start_x + min_dim]
    return cv2.resize(crop, (target_size[1], target_size[0]))


def extract_frames(video_path, num_frames=10, target_size=(224, 224), enable_face_crop=True):
    """
    Extract frames from a video file with optional face cropping.
    
    Args:
        video_path (str): Path to video file
        num_frames (int): Number of frames to extract (evenly spaced)
        target_size (tuple): Size to resize frames to (height, width)
        enable_face_crop (bool): Whether to perform OpenCV face detection & cropping
    
    Returns:
        np.ndarray: Array of extracted frames with shape (num_frames, height, width, 3)
                   Returns None if video cannot be read
    """
    try:
        if not HAS_CV2:
            print("Notice: OpenCV (cv2) is not installed.")
            return None

        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print(f"Error: Cannot open video file {video_path}")
            return None
        
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        if total_frames == 0:
            print(f"Error: Video has no frames {video_path}")
            cap.release()
            return None
        
        # Calculate frame indices to extract (evenly spaced)
        frame_indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)
        
        frames = []
        
        for frame_idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            ret, frame = cap.read()
            
            if ret:
                if enable_face_crop:
                    processed_frame = crop_face(frame, padding=0.2, target_size=target_size)
                else:
                    processed_frame = cv2.resize(frame, (target_size[1], target_size[0]))
                
                if processed_frame is not None:
                    frames.append(processed_frame)
        
        cap.release()
        
        if len(frames) == 0:
            print(f"Warning: No frames extracted from {video_path}")
            return None
        
        return np.array(frames)
    
    except Exception as e:
        print(f"Error extracting frames from {video_path}: {str(e)}")
        return None


def preprocess_frames(frames):
    """
    Normalize frames to [0, 1] range.
    
    Args:
        frames (np.ndarray): Array of frames with shape (num_frames, height, width, 3)
    
    Returns:
        np.ndarray: Normalized frames
    """
    if frames is None:
        return None
    
    return frames.astype('float32') / 255.0


def load_dataset(dataset_path, num_frames=10, target_size=(128, 128), max_videos=None):
    """
    Load entire dataset from folder structure.
    
    Args:
        dataset_path (str): Path to dataset folder (should contain 'real' and 'fake' folders)
        num_frames (int): Number of frames to extract per video
        target_size (tuple): Size to resize frames to
        max_videos (int): Maximum number of videos to load per class (None = all)
    
    Returns:
        tuple: (frames_list, labels_list) where labels are 0 for real, 1 for fake
    """
    frames_list = []
    labels_list = []
    
    dataset_path = Path(dataset_path)
    
    # Load real videos (label = 0)
    real_path = dataset_path / 'real'
    if real_path.exists():
        real_videos = sorted(list(real_path.glob('*.*')))[:max_videos]
        print(f"Loading {len(real_videos)} real videos...")
        
        for i, video_file in enumerate(real_videos):
            frames = extract_frames(str(video_file), num_frames, target_size)
            if frames is not None:
                frames = preprocess_frames(frames)
                frames_list.append(frames)
                labels_list.append(0)  # Real = 0
                if (i + 1) % 5 == 0:
                    print(f"  Loaded {i + 1} real videos...")
    
    # Load fake videos (label = 1)
    fake_path = dataset_path / 'fake'
    if fake_path.exists():
        fake_videos = sorted(list(fake_path.glob('*.*')))[:max_videos]
        print(f"Loading {len(fake_videos)} fake videos...")
        
        for i, video_file in enumerate(fake_videos):
            frames = extract_frames(str(video_file), num_frames, target_size)
            if frames is not None:
                frames = preprocess_frames(frames)
                frames_list.append(frames)
                labels_list.append(1)  # Fake = 1
                if (i + 1) % 5 == 0:
                    print(f"  Loaded {i + 1} fake videos...")
    
    print(f"Total videos loaded: {len(frames_list)}")
    
    if len(frames_list) == 0:
        print("No videos found in dataset!")
        return None, None
    
    # Reshape data: (num_videos, num_frames, height, width, 3) -> (num_videos*num_frames, height, width, 3)
    # This treats each frame as a separate training sample
    X = np.vstack(frames_list)
    y = np.repeat(labels_list, num_frames)
    
    print(f"Dataset shape: X={X.shape}, y={y.shape}")
    print(f"Real videos: {labels_list.count(0)}, Fake videos: {labels_list.count(1)}")
    
    return X, y


def prepare_frames_for_prediction(frames):
    """
    Prepare extracted frames for model prediction.
    
    Args:
        frames (np.ndarray): Extracted frames with shape (num_frames, height, width, 3)
    
    Returns:
        np.ndarray: Preprocessed frames ready for prediction
    """
    if frames is None:
        return None
    
    return preprocess_frames(frames)


def load_faceforensics_dataset(dataset_path, num_frames=10, target_size=(128, 128), max_videos=None):
    """
    Load dataset from FaceForensics++ folder structure.
    
    Expected structure:
        FaceForensics++_C23/
        ├── original/           (Real videos - label 0)
        ├── Deepfakes/          (Fake videos - label 1)
        ├── Face2Face/          (Fake videos - label 1)
        ├── FaceShifter/        (Fake videos - label 1)
        ├── FaceSwap/           (Fake videos - label 1)
        └── NeuralTextures/     (Fake videos - label 1)
    
    Args:
        dataset_path (str): Path to FaceForensics++ folder
        num_frames (int): Number of frames to extract per video
        target_size (tuple): Size to resize frames to
        max_videos (int): Maximum number of videos to load per class
    
    Returns:
        tuple: (frames_list, labels_list)
    """
    frames_list = []
    labels_list = []
    
    dataset_path = Path(dataset_path)
    
    # REAL videos from 'original' folder (label = 0)
    print("Loading REAL videos from 'original' folder...")
    real_path = dataset_path / 'original'
    if real_path.exists():
        real_videos = sorted(list(real_path.glob('*.*')))[:max_videos]
        print(f"Found {len(real_videos)} real videos")
        
        for i, video_file in enumerate(real_videos):
            frames = extract_frames(str(video_file), num_frames, target_size)
            if frames is not None:
                frames = preprocess_frames(frames)
                frames_list.append(frames)
                labels_list.append(0)  # Real = 0
                if (i + 1) % 5 == 0:
                    print(f"  Processed {i + 1} real videos...")
    
    # FAKE videos from multiple deepfake folders (label = 1)
    fake_folders = ['Deepfakes', 'Face2Face', 'FaceShifter', 'FaceSwap', 'NeuralTextures', 'DeepFakeDetection']
    
    for folder_name in fake_folders:
        fake_path = dataset_path / folder_name
        if fake_path.exists():
            print(f"\nLoading FAKE videos from '{folder_name}' folder...")
            fake_videos = sorted(list(fake_path.glob('*.*')))[:max_videos]
            print(f"Found {len(fake_videos)} deepfake videos")
            
            for i, video_file in enumerate(fake_videos):
                frames = extract_frames(str(video_file), num_frames, target_size)
                if frames is not None:
                    frames = preprocess_frames(frames)
                    frames_list.append(frames)
                    labels_list.append(1)  # Fake = 1
                    if (i + 1) % 5 == 0:
                        print(f"  Processed {i + 1} deepfake videos from {folder_name}...")
    
    print(f"\n[OK] Total videos loaded: {len(frames_list)}")
    
    if len(frames_list) == 0:
        print("No videos found in FaceForensics dataset!")
        return None, None
    
    # Reshape data
    X = np.vstack(frames_list)
    y = np.repeat(labels_list, num_frames)
    
    print(f"Dataset shape: X={X.shape}, y={y.shape}")
    print(f"Real samples: {(y == 0).sum()}, Fake samples: {(y == 1).sum()}")
    
    return X, y
