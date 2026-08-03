"""
TrustShield AI - Chunked Batch Training Script for FaceForensics++ Dataset
Trains in memory-safe chunks (e.g. 50 videos per batch) to prevent system lag and RAM overflow.
"""

import sys
import gc
import numpy as np
import os
from pathlib import Path
import matplotlib.pyplot as plt

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from utils import extract_frames, preprocess_frames
from model import build_model, build_model_light, build_transfer_model, unfreeze_for_finetuning
import tensorflow as tf
from tensorflow import keras


def get_all_faceforensics_video_paths(faceforensics_path):
    """Collect all real and fake video paths from FaceForensics++ directory structure."""
    dataset_path = Path(faceforensics_path)
    
    real_paths = []
    real_dir = dataset_path / 'original'
    if real_dir.exists():
        real_paths = sorted(list(real_dir.glob('*.*')))
        
    fake_folders = ['Deepfakes', 'Face2Face', 'FaceShifter', 'FaceSwap', 'NeuralTextures', 'DeepFakeDetection']
    fake_paths = []
    for f_folder in fake_folders:
        f_dir = dataset_path / f_folder
        if f_dir.exists():
            fake_paths.extend(sorted(list(f_dir.glob('*.*'))))
            
    return real_paths, fake_paths


def process_video_batch(video_list, labels_list, num_frames=10, target_size=(224, 224), enable_face_crop=True):
    """Extract and preprocess frames for a specific batch of videos."""
    frames_list = []
    valid_labels = []
    
    for v_path, label in zip(video_list, labels_list):
        frames = extract_frames(str(v_path), num_frames=num_frames, target_size=target_size, enable_face_crop=enable_face_crop)

        if frames is not None and len(frames) > 0:
            frames = preprocess_frames(frames)
            frames_list.append(frames)
            valid_labels.append(label)
            
    if len(frames_list) == 0:
        return None, None
        
    X = np.vstack(frames_list)
    y = np.repeat(valid_labels, num_frames)
    return X, y


def train_faceforensics_chunked(
    faceforensics_path="FaceForensics++_C23",
    model_save_path="models/deepfake_model.h5",
    use_transfer_learning=True,
    use_light_model=False,
    epochs=1,
    videos_per_chunk=50,
    max_total_videos=1500
):
    """
    Memory-safe Chunked Batch Training Function with Face Cropping & Transfer Learning.
    Loads and trains on small video chunks to keep RAM usage low and system smooth.
    """
    print("\n" + "="*60)
    print("TrustShield AI - Transfer Learning Memory-Safe Training Engine")
    print("="*60 + "\n")
    
    real_paths, fake_paths = get_all_faceforensics_video_paths(faceforensics_path)
    
    if len(real_paths) == 0 and len(fake_paths) == 0:
        print(f"ERROR: No videos found in {faceforensics_path}!")
        return
        
    print(f"[OK] Total Real Videos Found: {len(real_paths)}")
    print(f"[OK] Total Fake Videos Found: {len(fake_paths)}")
    
    # Cap total videos if specified (e.g. 1500 videos = 30 chunks)
    if max_total_videos is not None:
        real_paths = real_paths[:max_total_videos // 2]
        fake_paths = fake_paths[:max_total_videos // 2]
        print(f"[INFO] Capped dataset to {len(real_paths)} Real and {len(fake_paths)} Fake videos.")
        
    # Build fresh Transfer Learning or standard model instance
    target_size = (224, 224) if use_transfer_learning else (128, 128)
    
    if use_transfer_learning:
        print("[INFO] Building fresh MobileNetV2 Transfer Learning Model (Input: 224x224)...")
        model, _ = build_transfer_model(model_type='mobilenet', input_shape=(224, 224, 3))
    elif use_light_model:
        print("[INFO] Building Lightweight CNN Model...")
        model = build_model_light(input_shape=(128, 128, 3))
    else:
        print("[INFO] Building Standard CNN Model...")
        model = build_model(input_shape=(128, 128, 3))
        
    print("\nModel Architecture:")
    model.summary()

    print()
    
    # Interleave real and fake items into combined pairs
    all_pairs = []
    r_idx, f_idx = 0, 0
    while r_idx < len(real_paths) or f_idx < len(fake_paths):
        if r_idx < len(real_paths):
            all_pairs.append((real_paths[r_idx], 0))
            r_idx += 1
        if f_idx < len(fake_paths):
            all_pairs.append((fake_paths[f_idx], 1))
            f_idx += 1
            
    total_videos = len(all_pairs)
    total_chunks = (total_videos + videos_per_chunk - 1) // videos_per_chunk
    
    print(f"[START] Training across {total_chunks} chunks ({videos_per_chunk} videos per chunk)...")
    print("=" * 60 + "\n")
    
    for epoch in range(epochs):
        print(f"\n>>> EPOCH [{epoch+1}/{epochs}] STARTING <<<\n")
        
        for chunk_idx in range(total_chunks):
            start_i = chunk_idx * videos_per_chunk
            end_i = min(start_i + videos_per_chunk, total_videos)
            
            chunk_pairs = all_pairs[start_i:end_i]
            v_paths = [p for p, label in chunk_pairs]
            v_labels = [label for p, label in chunk_pairs]
            
            print(f"⌛ Chunk [{chunk_idx+1}/{total_chunks}]: Processing videos #{start_i+1} to #{end_i}...")
            
            X_chunk, y_chunk = process_video_batch(v_paths, v_labels, target_size=target_size)
            
            if X_chunk is not None and len(X_chunk) > 0:
                # Train on chunk
                model.fit(
                    X_chunk, y_chunk,
                    epochs=1,
                    batch_size=32,
                    verbose=1,
                    shuffle=True
                )
                
                # Checkpoint save after each chunk
                os.makedirs(os.path.dirname(model_save_path) or '.', exist_ok=True)
                model.save(model_save_path)
                print(f"  ✓ Chunk {chunk_idx+1}/{total_chunks} complete. Checkpoint saved to {model_save_path}\n")
            
            # Explicit Garbage Collection to keep RAM low
            del X_chunk, y_chunk
            gc.collect()
            
    print("="*60)
    print(f"✅ Target of {total_chunks} Chunks (1500 Videos) Reached! Training Stopped Cleanly.")
    print("="*60 + "\n")
    return model


if __name__ == "__main__":
    """
    Run Chunked Training capped at 30 Chunks (1,500 Videos total) as requested by user.
    """
    train_faceforensics_chunked(
        faceforensics_path="FaceForensics++_C23",
        model_save_path="models/deepfake_model.h5",
        use_light_model=False,
        epochs=1,
        videos_per_chunk=50,       # 50 videos per chunk
        max_total_videos=1500      # Exactly 30 Chunks (1500 Videos total)
    )
