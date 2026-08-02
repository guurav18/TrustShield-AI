"""
Pro Version Training Script - For Pre-organized FaceForensics Data
This script works with your existing folder structure where:
- Each folder contains real/ and fake/ subfolders with videos
"""

import numpy as np
import os
from pathlib import Path
import matplotlib.pyplot as plt
import shutil

from utils import extract_frames, preprocess_frames
from model import build_model, build_model_light
import tensorflow as tf
from tensorflow import keras


def load_pro_dataset(base_path, num_frames=10, target_size=(128, 128), max_videos=None):
    """
    Load dataset from organized folder structure.
    Supports multiple folder formats:
    
    Format 1:
        FaceForensics/
        ├── folder1/
        │   ├── real/
        │   └── fake/
        ├── folder2/
        │   ├── real/
        │   └── fake/
        ...
    
    Format 2 (Current):
        FaceForensics++_C23/
        ├── original/ (real)
        ├── Deepfakes/ (fake)
        ├── Face2Face/ (fake)
        ...
    
    Args:
        base_path (str): Base path to dataset
        num_frames (int): Frames per video
        target_size (tuple): Frame size
        max_videos (int): Max videos per folder
    
    Returns:
        tuple: (X, y) - training data and labels
    """
    frames_list = []
    labels_list = []
    
    base_path = Path(base_path)
    
    print("\n" + "="*60)
    print("Loading PRO Dataset")
    print("="*60 + "\n")
    
    # Real videos - From 'original' or 'real' folders
    real_paths = [
        base_path / 'original',
        base_path / 'real'
    ]
    
    print("📹 Loading REAL videos...")
    total_real = 0
    for real_path in real_paths:
        if real_path.exists():
            videos = sorted(list(real_path.glob('*.*')))[:max_videos]
            if videos:
                print(f"  Found {len(videos)} in {real_path.name}/")
                for i, video_file in enumerate(videos):
                    try:
                        frames = extract_frames(str(video_file), num_frames, target_size)
                        if frames is not None:
                            frames = preprocess_frames(frames)
                            frames_list.append(frames)
                            labels_list.append(0)  # Real = 0
                            total_real += 1
                            if (i + 1) % 10 == 0:
                                print(f"    ⏳ Loaded {i + 1}/{len(videos)}...")
                    except Exception as e:
                        pass  # Skip broken videos silently
                print(f"  ✓ Loaded {total_real} real videos\n")
    
    # Fake videos - From 'fake' and other deepfake folders
    fake_folders = [
        base_path / 'fake',
        base_path / 'Deepfakes',
        base_path / 'Face2Face',
        base_path / 'FaceSwap',
        base_path / 'FaceShifter',
        base_path / 'NeuralTextures',
        base_path / 'DeepFakeDetection'
    ]
    
    print("🎭 Loading FAKE videos...")
    total_fake = 0
    for fake_path in fake_folders:
        if fake_path.exists():
            videos = sorted(list(fake_path.glob('*.*')))[:max_videos]
            if videos:
                print(f"  Found {len(videos)} in {fake_path.name}/")
                for i, video_file in enumerate(videos):
                    try:
                        frames = extract_frames(str(video_file), num_frames, target_size)
                        if frames is not None:
                            frames = preprocess_frames(frames)
                            frames_list.append(frames)
                            labels_list.append(1)  # Fake = 1
                            total_fake += 1
                            if (i + 1) % 10 == 0:
                                print(f"    ⏳ Loaded {i + 1}/{len(videos)}...")
                    except Exception as e:
                        pass  # Skip broken videos silently
                print(f"  ✓ Loaded {total_fake} fake videos\n")
    
    print("="*60)
    print(f"✅ TOTAL: {total_real} real videos + {total_fake} fake videos\n")
    
    if len(frames_list) == 0:
        print("❌ No videos loaded!")
        return None, None
    
    # Combine all frames
    X = np.vstack(frames_list)
    y = np.repeat(labels_list, num_frames)
    
    print(f"📊 Dataset Shape: X={X.shape}, y={y.shape}")
    print(f"   Real samples: {(y == 0).sum()}")
    print(f"   Fake samples: {(y == 1).sum()}\n")
    
    return X, y


def train_pro_model(dataset_path, model_save_path, use_light_model=False, epochs=20, batch_size=32, max_videos=None):
    """
    Train model with pro dataset.
    """
    
    print("\n" + "="*60)
    print("🛡️ TrustShield AI - PRO VERSION Training")
    print("="*60 + "\n")
    
    dataset_path = Path(dataset_path)
    if not dataset_path.exists():
        print(f"❌ Dataset path {dataset_path} does not exist!")
        return
    
    # Load dataset
    X, y = load_pro_dataset(str(dataset_path), num_frames=10, target_size=(128, 128), max_videos=max_videos)
    
    if X is None:
        return
    
    # Build model
    print("🧠 Building model...")
    if use_light_model:
        model = build_model_light(input_shape=(128, 128, 3))
        print("   Using LIGHT model (faster)\n")
    else:
        model = build_model(input_shape=(128, 128, 3))
        print("   Using STANDARD model\n")
    
    print("Model Architecture:")
    model.summary()
    print()
    
    # Train
    print(f"⏳ Training for {epochs} epochs...")
    print("=" * 60)
    
    history = model.fit(
        X, y,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.2,
        verbose=1,
        shuffle=True
    )
    
    # Save
    os.makedirs(os.path.dirname(model_save_path) or '.', exist_ok=True)
    model.save(model_save_path)
    print(f"\n✅ Model saved: {model_save_path}")
    
    # Plot
    plot_history(history, "training_history_pro.png")
    
    print("\n" + "="*60)
    print("✅ Training Complete!")
    print("="*60 + "\n")
    
    return model, history


def plot_history(history, filename):
    """Plot training history."""
    try:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        
        axes[0].plot(history.history['loss'], label='Training Loss', linewidth=2)
        axes[0].plot(history.history['val_loss'], label='Validation Loss', linewidth=2)
        axes[0].set_title('Model Loss', fontsize=12)
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Loss')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        axes[1].plot(history.history['accuracy'], label='Training Accuracy', linewidth=2)
        axes[1].plot(history.history['val_accuracy'], label='Validation Accuracy', linewidth=2)
        axes[1].set_title('Model Accuracy', fontsize=12)
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Accuracy')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=100, bbox_inches='tight')
        print(f"✅ Plot saved: {filename}")
        plt.close()
    except Exception as e:
        print(f"⚠️ Could not plot: {e}")


if __name__ == "__main__":
    """
    PRO VERSION TRAINING
    Automatically detects your dataset structure and trains
    """
    
    # Try to find dataset in common locations
    dataset_paths = [
        "FaceForensics++_C23",
        "FaceForensics",
        "dataset"
    ]
    
    dataset_path = None
    for path in dataset_paths:
        if Path(path).exists():
            dataset_path = path
            break
    
    if dataset_path is None:
        print("❌ No dataset folder found!")
        print("Expected one of:", dataset_paths)
        exit(1)
    
    print(f"✅ Found dataset: {dataset_path}\n")
    
    model_save_path = "models/deepfake_model.h5"
    
    # Training options - CUSTOMIZE HERE
    USE_LIGHT_MODEL = False    # False = better accuracy, True = faster training
    EPOCHS = 20                 # Higher = better accuracy but slower
    BATCH_SIZE = 32            # Can adjust based on RAM
    MAX_VIDEOS = 500           # Medium training: 500 videos (~35-45 min)
    
    print("⚙️ Training Configuration:")
    print(f"   Model: {'LIGHT (Fast)' if USE_LIGHT_MODEL else 'STANDARD (Accurate)'}")
    print(f"   Epochs: {EPOCHS}")
    print(f"   Batch Size: {BATCH_SIZE}")
    print(f"   Max Videos per folder: {MAX_VIDEOS if MAX_VIDEOS else 'All'}")
    print()
    
    # Train
    train_pro_model(
        dataset_path=dataset_path,
        model_save_path=model_save_path,
        use_light_model=USE_LIGHT_MODEL,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        max_videos=MAX_VIDEOS
    )
    
    print("\n" + "="*60)
    print("🎉 Next Steps:")
    print("="*60)
    print("1. Run the web app:")
    print("   streamlit run app.py")
    print()
    print("2. Upload videos to analyze!")
    print("="*60 + "\n")
