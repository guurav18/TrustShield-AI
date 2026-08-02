"""
⚡ QUICK TRAIN - Fast Testing Version
Sirf kuch videos use karke test karo
"""

import numpy as np
import os
from pathlib import Path
import matplotlib.pyplot as plt

from utils import extract_frames, preprocess_frames
from model import build_model, build_model_light
import tensorflow as tf
from tensorflow import keras


def load_quick_dataset(base_path, num_frames=10, target_size=(128, 128), max_per_folder=20):
    """
    Quick dataset loader - sirf limited videos load karta hai
    """
    frames_list = []
    labels_list = []
    
    base_path = Path(base_path)
    
    print("\n" + "="*60)
    print("⚡ QUICK TRAINING - Fast Version")
    print("="*60 + "\n")
    
    # Real videos
    print("📹 Loading REAL videos (max 20)...")
    real_path = base_path / 'original'
    if real_path.exists():
        videos = sorted(list(real_path.glob('*.*')))[:max_per_folder]
        print(f"  Found {len(videos)} real videos")
        
        loaded = 0
        for i, video_file in enumerate(videos):
            try:
                frames = extract_frames(str(video_file), num_frames, target_size)
                if frames is not None:
                    frames = preprocess_frames(frames)
                    frames_list.append(frames)
                    labels_list.append(0)
                    loaded += 1
                    print(f"  ✓ {loaded}/{len(videos)}", end='\r')
            except:
                pass
        print(f"  ✓ Loaded {loaded} real videos     \n")
    
    # Fake videos
    print("🎭 Loading FAKE videos (max 20 per type)...")
    fake_folders = [
        'Deepfakes', 'Face2Face', 'FaceSwap', 'FaceShifter', 'NeuralTextures'
    ]
    
    total_fake = 0
    for folder_name in fake_folders:
        fake_path = base_path / folder_name
        if fake_path.exists():
            videos = sorted(list(fake_path.glob('*.*')))[:max_per_folder]
            if videos:
                print(f"  {folder_name}: Loading {len(videos)}...", end='\r')
                
                loaded = 0
                for video_file in videos:
                    try:
                        frames = extract_frames(str(video_file), num_frames, target_size)
                        if frames is not None:
                            frames = preprocess_frames(frames)
                            frames_list.append(frames)
                            labels_list.append(1)
                            loaded += 1
                            total_fake += 1
                    except:
                        pass
                print(f"  ✓ {folder_name}: {loaded} loaded          ")
    
    print()
    
    if len(frames_list) == 0:
        print("❌ No videos loaded!")
        return None, None
    
    X = np.vstack(frames_list)
    y = np.repeat(labels_list, num_frames)
    
    print(f"✅ Dataset Ready!")
    print(f"   Real samples: {(y == 0).sum()}")
    print(f"   Fake samples: {(y == 1).sum()}")
    print(f"   Total shape: {X.shape}\n")
    
    return X, y


if __name__ == "__main__":
    base_path = "FaceForensics++_C23"
    model_save_path = "models/deepfake_model.h5"
    
    # Load quick dataset
    X, y = load_quick_dataset(base_path, max_per_folder=20)
    
    if X is None:
        exit(1)
    
    # Build light model
    print("🧠 Building LIGHT model (fast)...")
    model = build_model_light(input_shape=(128, 128, 3))
    model.summary()
    print()
    
    # Quick train
    print("⏳ Training (5 epochs, fast)...")
    print("=" * 60)
    
    history = model.fit(
        X, y,
        epochs=5,
        batch_size=32,
        validation_split=0.2,
        verbose=1,
        shuffle=True
    )
    
    # Save
    os.makedirs('models', exist_ok=True)
    model.save(model_save_path)
    print(f"\n✅ Model saved: {model_save_path}")
    
    print("\n" + "="*60)
    print("✅ Quick Training Complete!")
    print("="*60)
    print("\nNow run:")
    print("  streamlit run app.py")
    print("="*60 + "\n")
