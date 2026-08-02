"""
Training script for TrustShield AI Deepfake Detection System
Loads data, trains the model, and saves it
"""

import numpy as np
import os
from pathlib import Path
import matplotlib.pyplot as plt

from utils import load_dataset, extract_frames, preprocess_frames
from model import build_model, build_model_light
import tensorflow as tf
from tensorflow import keras


def train_model(dataset_path, model_save_path, use_light_model=False, epochs=20, batch_size=32, max_videos=None):
    """
    Train the deepfake detection model.
    
    Args:
        dataset_path (str): Path to dataset folder
        model_save_path (str): Path to save trained model
        use_light_model (bool): Use lighter model for faster training
        epochs (int): Number of training epochs
        batch_size (int): Batch size for training
        max_videos (int): Maximum videos per class to load (for testing)
    """
    
    print("\n" + "="*60)
    print("TrustShield AI - Training Script")
    print("="*60 + "\n")
    
    # Check if dataset exists
    dataset_path = Path(dataset_path)
    if not dataset_path.exists():
        print(f"ERROR: Dataset path {dataset_path} does not exist!")
        return
    
    # Load dataset
    print("Loading dataset...")
    X, y = load_dataset(str(dataset_path), num_frames=10, target_size=(128, 128), max_videos=max_videos)
    
    if X is None or len(X) == 0:
        print("ERROR: No data loaded! Please add videos to dataset/real and dataset/fake folders.")
        return
    
    print(f"Dataset loaded successfully!")
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
    """
    Plot training history (loss and accuracy).
    
    Args:
        history: Keras training history object
    """
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
        plt.savefig('training_history.png', dpi=100)
        print("✓ Training history plot saved as 'training_history.png'")
        plt.close()
    except Exception as e:
        print(f"Could not plot training history: {e}")


if __name__ == "__main__":
    """
    Run training with default settings.
    """
    dataset_path = "dataset"
    model_save_path = "models/deepfake_model.h5"
    
    # Train the model
    # Set max_videos=2 for quick testing with a few videos
    # Set max_videos=None to train on all available videos
    train_model(
        dataset_path=dataset_path,
        model_save_path=model_save_path,
        use_light_model=False,  # Set to True for faster training
        epochs=20,
        batch_size=32,
        max_videos=None  # Change to small number for testing
    )
