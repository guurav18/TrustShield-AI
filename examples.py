"""
Example usage of TrustShield AI
Demonstrates how to use the system programmatically
"""

import os
from pathlib import Path
from predict import DeepfakeDetector
from train import train_model
from utils import load_dataset, extract_frames
from config import MODEL_PATH, DATASET_PATH


def example_1_verify_setup():
    """
    Example 1: Verify that the system is set up correctly
    """
    print("\n" + "="*60)
    print("Example 1: Verify Setup")
    print("="*60)
    
    # Check required directories
    required_dirs = [
        "dataset",
        "dataset/real",
        "dataset/fake",
        "models"
    ]
    
    print("\nChecking directories...")
    for dir_path in required_dirs:
        exists = os.path.exists(dir_path)
        status = "✓" if exists else "✗"
        print(f"  {status} {dir_path}")
    
    # Check for videos in dataset
    real_count = len(list(Path("dataset/real").glob("*.*")))
    fake_count = len(list(Path("dataset/fake").glob("*.*")))
    
    print(f"\nDataset status:")
    print(f"  Real videos: {real_count}")
    print(f"  Fake videos: {fake_count}")
    
    if real_count == 0 or fake_count == 0:
        print("\n⚠️  Add videos to dataset/real and dataset/fake folders first!")
        return False
    
    print("\n✓ Setup looks good!")
    return True


def example_2_load_dataset():
    """
    Example 2: Load and inspect dataset
    """
    print("\n" + "="*60)
    print("Example 2: Load Dataset")
    print("="*60)
    
    print("\nLoading dataset...")
    X, y = load_dataset(DATASET_PATH, num_frames=10, max_videos=5)
    
    if X is not None:
        print(f"\n✓ Dataset loaded successfully!")
        print(f"  X shape: {X.shape}  (samples, height, width, channels)")
        print(f"  y shape: {y.shape}  (labels)")
        print(f"  Data type: {X.dtype}")
        print(f"  Value range: [{X.min():.3f}, {X.max():.3f}]")
        print(f"  Real samples: {(y == 0).sum()}")
        print(f"  Fake samples: {(y == 1).sum()}")
    else:
        print("✗ Failed to load dataset")
        return False
    
    return True


def example_3_extract_frames():
    """
    Example 3: Extract frames from a single video
    """
    print("\n" + "="*60)
    print("Example 3: Extract Frames from Video")
    print("="*60)
    
    # Find a sample video
    real_videos = list(Path("dataset/real").glob("*.*"))
    
    if not real_videos:
        print("No videos found in dataset/real/")
        return False
    
    video_path = str(real_videos[0])
    print(f"\nExtracting frames from: {video_path}")
    
    frames = extract_frames(video_path, num_frames=5, target_size=(128, 128))
    
    if frames is not None:
        print(f"\n✓ Frames extracted!")
        print(f"  Shape: {frames.shape}  (frames, height, width, channels)")
        print(f"  Data type: {frames.dtype}")
        print(f"  Value range: [{frames.min()}, {frames.max()}]")
    else:
        print("✗ Failed to extract frames")
        return False
    
    return True


def example_4_train_model():
    """
    Example 4: Train model with custom settings
    """
    print("\n" + "="*60)
    print("Example 4: Train Model")
    print("="*60)
    
    print("\nThis will train the model. This may take a while...")
    print("For quick testing, using max_videos=2 per class\n")
    
    # Uncomment to train:
    # train_model(
    #     dataset_path=DATASET_PATH,
    #     model_save_path=MODEL_PATH,
    #     use_light_model=True,
    #     epochs=5,
    #     batch_size=32,
    #     max_videos=2
    # )
    
    print("(Training code is commented out - uncomment to run)")
    print("Run 'python train.py' to train the model")


def example_5_predict_single_video():
    """
    Example 5: Make prediction on a single video
    """
    print("\n" + "="*60)
    print("Example 5: Predict on Video")
    print("="*60)
    
    # Check if model exists
    if not os.path.exists(MODEL_PATH):
        print(f"\n✗ Model not found at {MODEL_PATH}")
        print("Run 'python train.py' first to train the model")
        return False
    
    # Find a test video
    real_videos = list(Path("dataset/real").glob("*.*"))
    fake_videos = list(Path("dataset/fake").glob("*.*"))
    
    if not real_videos and not fake_videos:
        print("No test videos found")
        return False
    
    print("\nLoading model...")
    detector = DeepfakeDetector(MODEL_PATH)
    
    # Test on real video
    if real_videos:
        video_path = str(real_videos[0])
        print(f"\nPredicting on REAL video: {Path(video_path).name}")
        result = detector.predict_video(video_path, num_frames=10)
        
        if result:
            print(f"  Classification: {'FAKE ⚠️' if result['is_fake'] else 'REAL ✓'}")
            print(f"  Confidence: {result['confidence']:.2f}%")
            print(f"  Prediction score: {result['prediction']:.4f}")
            print(f"  Frames analyzed: {result['frames_analyzed']}")
    
    # Test on fake video
    if fake_videos:
        video_path = str(fake_videos[0])
        print(f"\nPredicting on FAKE video: {Path(video_path).name}")
        result = detector.predict_video(video_path, num_frames=10)
        
        if result:
            print(f"  Classification: {'FAKE ⚠️' if result['is_fake'] else 'REAL ✓'}")
            print(f"  Confidence: {result['confidence']:.2f}%")
            print(f"  Prediction score: {result['prediction']:.4f}")
            print(f"  Frames analyzed: {result['frames_analyzed']}")
    
    return True


def example_6_batch_prediction():
    """
    Example 6: Batch prediction on multiple videos
    """
    print("\n" + "="*60)
    print("Example 6: Batch Prediction")
    print("="*60)
    
    if not os.path.exists(MODEL_PATH):
        print(f"Model not found at {MODEL_PATH}")
        return False
    
    print("\nLoading model...")
    detector = DeepfakeDetector(MODEL_PATH)
    
    # Get all videos
    real_videos = list(Path("dataset/real").glob("*.*"))[:3]
    fake_videos = list(Path("dataset/fake").glob("*.*"))[:3]
    
    all_results = []
    
    print("\nAnalyzing real videos:")
    for video_path in real_videos:
        result = detector.predict_video(str(video_path), num_frames=10)
        if result:
            all_results.append({
                'video': video_path.name,
                'label': 'REAL',
                'prediction': result['is_fake'],
                'confidence': result['confidence']
            })
            print(f"  {video_path.name}: {'FAKE ⚠️' if result['is_fake'] else 'REAL ✓'} ({result['confidence']:.1f}%)")
    
    print("\nAnalyzing fake videos:")
    for video_path in fake_videos:
        result = detector.predict_video(str(video_path), num_frames=10)
        if result:
            all_results.append({
                'video': video_path.name,
                'label': 'FAKE',
                'prediction': result['is_fake'],
                'confidence': result['confidence']
            })
            print(f"  {video_path.name}: {'FAKE ⚠️' if result['is_fake'] else 'REAL ✓'} ({result['confidence']:.1f}%)")
    
    # Calculate accuracy
    if all_results:
        correct = 0
        for result in all_results:
            actual_is_fake = result['label'] == 'FAKE'
            predicted_is_fake = result['prediction']
            if actual_is_fake == predicted_is_fake:
                correct += 1
        
        accuracy = (correct / len(all_results)) * 100
        print(f"\nAccuracy: {accuracy:.1f}% ({correct}/{len(all_results)})")
    
    return True


def main():
    """
    Run all examples
    """
    print("\n" + "="*60)
    print("TrustShield AI - Usage Examples")
    print("="*60)
    
    examples = [
        ("Verify Setup", example_1_verify_setup),
        ("Load Dataset", example_2_load_dataset),
        ("Extract Frames", example_3_extract_frames),
        ("Train Model", example_4_train_model),
        ("Predict Single Video", example_5_predict_single_video),
        ("Batch Prediction", example_6_batch_prediction),
    ]
    
    for i, (name, example_func) in enumerate(examples, 1):
        try:
            result = example_func()
            if not result and result is not None:
                print(f"\n⚠️  Example {i} requires setup (e.g., training, data)")
        except Exception as e:
            print(f"\n✗ Example {i} error: {str(e)}")
    
    print("\n" + "="*60)
    print("Examples Complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Add videos to dataset/real and dataset/fake")
    print("2. Run: python train.py")
    print("3. Run: streamlit run app.py")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
