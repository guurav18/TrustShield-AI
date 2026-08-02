"""
Training script for FaceForensics++ dataset
Uses videos from: original/, Deepfakes/, Face2Face/, FaceSwap/, etc.
"""

import numpy as np
import os
from pathlib import Path
import matplotlib.pyplot as plt

from utils import load_faceforensics_dataset
from model import build_model, build_model_light
import tensorflow as tf
from tensorflow import keras


def train_faceforensics(faceforensics_path, model_save_path, use_light_model=False, epochs=20, batch_size=32, max_videos=None):
    """
    Train model using FaceForensics++ dataset.
    
    Args:
        faceforensics_path (str): Path to FaceForensics++_C23 folder
        model_save_path (str): Path to save trained model
        use_light_model (bool): Use lighter model for faster training
        epochs (int): Number of training epochs
        batch_size (int): Batch size for training
        max_videos (int): Maximum videos per folder to load
    """
    
    print("\n" + "="*60)
    print("TrustShield AI - FaceForensics Training Script")
    print("="*60 + "\n")
    
    # Check if dataset exists
    faceforensics_path = Path(faceforensics_path)
    if not faceforensics_path.exists():
        print(f"ERROR: Dataset path {faceforensics_path} does not exist!")
        return
    
    # Load dataset from FaceForensics structure
    print("Loading FaceForensics++ dataset...")
    print("This may take a few minutes...\n")
    
    X, y = load_faceforensics_dataset(
        str(faceforensics_path), 
        num_frames=10, 
        target_size=(128, 128), 
        max_videos=max_videos
    )
    
    if X is None or len(X) == 0:
        print("ERROR: No data loaded!")
        return
    
    print(f"\n✓ Dataset loaded successfully!")
    print(f"Training samples: {len(X)}")
    print(f"Real videos: {np.sum(y == 0) // 10}, Fake videos: {np.sum(y == 1) // 10}\n")
    
    # Build model
    print("Building model...")
    if use_light_model:
        model = build_model_light(input_shape=(128, 128, 3))
        print("Using LIGHT model (faster training)\n")
    else:
        model = build_model(input_shape=(128, 128, 3))
        print("Using STANDARD model\n")
    
    # Print model summary
    print("Model Architecture:")
    model.summary()
    print()
    
    # Train model
    print(f"Training model for {epochs} epochs...")
    print("=" * 60)
    
    history = model.fit(
        X, y,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.2,
        verbose=1,
        shuffle=True
    )
    
    # Save model
    os.makedirs(os.path.dirname(model_save_path) or '.', exist_ok=True)
    model.save(model_save_path)
    print(f"\n✓ Model saved to: {model_save_path}")
    
    # Plot training history
    plot_training_history(history)
    
    print("\n" + "="*60)
    print("Training Complete!")
    print("="*60 + "\n")
    
    return model, history


def plot_training_history(history):
    """Plot training history."""
    try:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        
        # Plot loss
        axes[0].plot(history.history['loss'], label='Training Loss')
        axes[0].plot(history.history['val_loss'], label='Validation Loss')
        axes[0].set_title('Model Loss')
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Loss')
        axes[0].legend()
        axes[0].grid(True)
        
        # Plot accuracy
        axes[1].plot(history.history['accuracy'], label='Training Accuracy')
        axes[1].plot(history.history['val_accuracy'], label='Validation Accuracy')
        axes[1].set_title('Model Accuracy')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Accuracy')
        axes[1].legend()
        axes[1].grid(True)
        
        plt.tight_layout()
        plt.savefig('training_history_faceforensics.png', dpi=100)
        print("✓ Training history plot saved as 'training_history_faceforensics.png'")
        plt.close()
    except Exception as e:
        print(f"Could not plot training history: {e}")


if __name__ == "__main__":
    """
    Train using FaceForensics++ dataset
    """
    faceforensics_path = "FaceForensics++_C23"
    model_save_path = "models/deepfake_model.h5"
    
    train_faceforensics(
        faceforensics_path=faceforensics_path,
        model_save_path=model_save_path,
        use_light_model=False,  # Set to True for faster training on CPU
        epochs=20,
        batch_size=32,
        max_videos=None  # Set to small number (e.g., 5) for quick testing
    )
