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


def extract_frames(video_path, num_frames=10, target_size=(128, 128)):
    """
    Extract frames from a video file.
    
    Args:
        video_path (str): Path to video file
        num_frames (int): Number of frames to extract (evenly spaced)
        target_size (tuple): Size to resize frames to (height, width)
    
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
                # Resize frame
                frame = cv2.resize(frame, (target_size[1], target_size[0]))
                frames.append(frame)
        
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
    fake_folders = ['Deepfakes', 'Face2Face', 'FaceShifter', 'FaceSwap', 'NeuralTextures']
    
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
    
    print(f"\n✓ Total videos loaded: {len(frames_list)}")
    
    if len(frames_list) == 0:
        print("No videos found in FaceForensics dataset!")
        return None, None
    
    # Reshape data
    X = np.vstack(frames_list)
    y = np.repeat(labels_list, num_frames)
    
    print(f"Dataset shape: X={X.shape}, y={y.shape}")
    print(f"Real samples: {(y == 0).sum()}, Fake samples: {(y == 1).sum()}")
    
    return X, y
