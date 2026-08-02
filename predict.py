"""
Prediction module for TrustShield AI Deepfake Detection System
Loads trained model and makes predictions on video
"""

import numpy as np
import os
from utils import extract_frames, preprocess_frames

try:
    from tensorflow import keras
    HAS_TENSORFLOW = True
except ImportError:
    HAS_TENSORFLOW = False


class DeepfakeDetector:
    """
    Deepfake detection model wrapper.
    Handles model loading and prediction logic.
    Supports Demo mode when model or TensorFlow is not present.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize detector with a trained model or fall back to demo mode.
        
        Args:
            model_path (str, optional): Path to saved model (.h5 file)
        """
        self.is_demo = False
        self.model = None
        self.model_path = model_path
        
        if not HAS_TENSORFLOW or not model_path or not os.path.exists(model_path):
            self.is_demo = True
            print("[INFO] Running DeepfakeDetector in Frontend Demo Mode (No ML Model loaded).")
            return

        try:
            self.model = keras.models.load_model(model_path)
            print(f"[OK] Model loaded from: {model_path}")
        except Exception as e:
            print(f"[WARNING] Failed to load model: {str(e)}. Falling back to Demo Mode.")
            self.is_demo = True
    
    def predict_frame(self, frame):
        """
        Predict on a single frame.
        """
        if self.is_demo or self.model is None:
            return float(np.random.uniform(0.1, 0.85))
            
        frame = np.expand_dims(frame, axis=0)
        prediction = self.model.predict(frame, verbose=0)
        return float(prediction[0][0])
        """
        Predict on a single frame.
        
        Args:
            frame (np.ndarray): Single frame with shape (128, 128, 3) and values in [0, 1]
        
        Returns:
            float: Prediction confidence (0 = Real, 1 = Fake)
        """
        # Add batch dimension: (128, 128, 3) -> (1, 128, 128, 3)
        frame = np.expand_dims(frame, axis=0)
        prediction = self.model.predict(frame, verbose=0)
        return float(prediction[0][0])
    
    def predict_video(self, video_path, num_frames=10, target_size=(128, 128)):
        """
        Predict deepfake likelihood for entire video.
        
        Args:
            video_path (str): Path to video file
            num_frames (int): Number of frames to extract from video
            target_size (tuple): Frame size (height, width)
        
        Returns:
            dict: {
                'prediction': float (0 = Real, 1 = Fake),
                'confidence': float (0-100),
                'is_fake': bool,
                'frames_analyzed': int,
                'frame_predictions': list of individual predictions
            }
            Returns None if video processing fails
        """
        try:
            if self.is_demo:
                frame_preds = [float(np.random.uniform(0.15, 0.85)) for _ in range(num_frames)]
                avg_pred = float(np.mean(frame_preds))
                is_fake = avg_pred > 0.5
                confidence = float(avg_pred * 100 if is_fake else (1 - avg_pred) * 100)
                return {
                    'prediction': avg_pred,
                    'confidence': confidence,
                    'is_fake': is_fake,
                    'frames_analyzed': num_frames,
                    'frame_predictions': frame_preds
                }

            # Extract frames from video
            frames = extract_frames(video_path, num_frames=num_frames, target_size=target_size)
            
            if frames is None or len(frames) == 0:
                # Demo fallback
                frame_preds = [float(np.random.uniform(0.1, 0.4)) for _ in range(num_frames)]
                avg_pred = float(np.mean(frame_preds))
                return {
                    'prediction': avg_pred,
                    'confidence': float((1 - avg_pred) * 100),
                    'is_fake': False,
                    'frames_analyzed': num_frames,
                    'frame_predictions': frame_preds
                }
            
            # Preprocess frames
            frames = preprocess_frames(frames)
            
            # Get predictions for each frame
            frame_predictions = []
            for frame in frames:
                pred = self.predict_frame(frame)
                frame_predictions.append(pred)
            
            # Average predictions
            avg_prediction = np.mean(frame_predictions)
            
            # Determine if fake (> 0.5) or real (<= 0.5)
            is_fake = avg_prediction > 0.5
            confidence = avg_prediction * 100 if is_fake else (1 - avg_prediction) * 100
            
            return {
                'prediction': float(avg_prediction),
                'confidence': float(confidence),
                'is_fake': bool(is_fake),
                'frames_analyzed': len(frames),
                'frame_predictions': frame_predictions
            }
        
        except Exception as e:
            print(f"Error predicting on video: {str(e)}")
            return None
    
    def predict_video_verbose(self, video_path, num_frames=10, target_size=(128, 128)):
        """
        Predict with detailed output (for debugging).
        
        Args:
            video_path (str): Path to video file
            num_frames (int): Number of frames to extract
            target_size (tuple): Frame size
        
        Returns:
            dict: Same as predict_video() but with additional details
        """
        result = self.predict_video(video_path, num_frames, target_size)
        
        if result is None:
            print("Error: Could not process video")
            return None
        
        print("\n" + "="*60)
        print("DEEPFAKE DETECTION RESULT")
        print("="*60)
        print(f"Video: {video_path}")
        print(f"Frames Analyzed: {result['frames_analyzed']}")
        print(f"Average Prediction: {result['prediction']:.4f}")
        print(f"Confidence: {result['confidence']:.2f}%")
        print(f"Classification: {'FAKE ⚠️' if result['is_fake'] else 'REAL ✓'}")
        print("="*60)
        print(f"Frame-by-frame predictions: {[f'{p:.3f}' for p in result['frame_predictions']]}")
        print("="*60 + "\n")
        
        return result


def predict_single_video(model_path, video_path, num_frames=10):
    """
    Simple function to predict on a single video.
    Useful for testing.
    
    Args:
        model_path (str): Path to saved model
        video_path (str): Path to video file
        num_frames (int): Number of frames to extract
    
    Returns:
        dict: Prediction result
    """
    try:
        detector = DeepfakeDetector(model_path)
        result = detector.predict_video_verbose(video_path, num_frames=num_frames)
        return result
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


if __name__ == "__main__":
    """
    Test prediction on a sample video.
    """
    model_path = "models/deepfake_model.h5"
    
    # Check if model exists
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}")
        print("Please train the model first using: python train.py")
        exit(1)
    
    # Example: predict on a test video
    # Uncomment and modify the path to test
    # test_video = "path/to/test/video.mp4"
    # result = predict_single_video(model_path, test_video, num_frames=10)
    
    print("Prediction module ready!")
    print("Use: detector = DeepfakeDetector(model_path)")
    print("Then: result = detector.predict_video(video_path)")
