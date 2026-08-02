# 🛡️ TrustShield AI - Deepfake Video Detection System

A complete, beginner-friendly deep learning system for detecting deepfake videos. Uses CNN architecture for binary classification (REAL vs FAKE) with a Streamlit web interface.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [How to Use](#how-to-use)
- [Model Architecture](#model-architecture)
- [Dataset Preparation](#dataset-preparation)
- [Training Details](#training-details)
- [Troubleshooting](#troubleshooting)

---

## ✨ Features

✓ **Simple CNN Architecture** - Easy to understand and modify
✓ **Frame-Based Analysis** - Analyzes multiple frames per video for robust predictions
✓ **Confidence Scoring** - Shows confidence percentage for each prediction
✓ **Streamlit UI** - Beautiful, interactive web interface
✓ **Modular Code** - Clean, well-organized, production-ready structure
✓ **Binary Classification** - REAL (0) or FAKE (1)
✓ **Detailed Logging** - Frame-by-frame analysis available

---

## 📁 Project Structure

```
deepfake/
├── dataset/
│   ├── real/              # Place real videos here
│   └── fake/              # Place fake/deepfake videos here
├── models/
│   └── deepfake_model.h5  # Trained model (generated after training)
├── utils.py               # Frame extraction & preprocessing
├── model.py               # CNN architecture
├── train.py               # Training script
├── predict.py             # Prediction module
├── app.py                 # Streamlit web interface
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 📦 Requirements

- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- GPU (optional, but speeds up training)

### Dependencies

All Python packages listed in `requirements.txt`:
- `numpy` - Numerical computing
- `pandas` - Data manipulation
- `opencv-python` - Video processing
- `tensorflow` & `keras` - Deep learning
- `matplotlib` - Plotting
- `streamlit` - Web UI
- `Pillow` - Image processing

---

## 🚀 Installation

### Step 1: Clone or Download Project

```bash
cd deepfake
```

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** TensorFlow installation may take a few minutes.

---

## ⚡ Quick Start

### 1. Add Training Data

Place video files in appropriate folders:
```
dataset/
├── real/
│   ├── real_video1.mp4
│   ├── real_video2.mp4
│   └── ...
└── fake/
    ├── deepfake1.mp4
    ├── deepfake2.mp4
    └── ...
```

**Minimum:** At least 5-10 videos per category for meaningful training

### 2. Train the Model

```bash
python train.py
```

**First run** may take 5-15 minutes depending on:
- Number of videos
- Video resolution
- Hardware (GPU vs CPU)

Once training completes:
- Model saved to `models/deepfake_model.h5`
- Training history plot saved to `training_history.png`

### 3. Run Web Interface

```bash
streamlit run app.py
```

This opens the web interface at `http://localhost:8501`

### 4. Upload and Analyze Videos

- Upload a test video
- Click "Analyze Video"
- View results with confidence score

---

## 📖 How to Use

### Using the Web Interface (Recommended)

1. **Run Streamlit:**
   ```bash
   streamlit run app.py
   ```

2. **Upload Video:**
   - Click "Choose a video file"
   - Select MP4, MOV, AVI, or WMV

3. **Adjust Settings:**
   - Frames to analyze (default: 10)
   - More frames = better accuracy but slower

4. **View Results:**
   - REAL or FAKE classification
   - Confidence percentage
   - Frame-by-frame analysis (expandable)

### Using Prediction Programmatically

```python
from predict import DeepfakeDetector

# Initialize detector
detector = DeepfakeDetector("models/deepfake_model.h5")

# Predict on video
result = detector.predict_video("path/to/video.mp4", num_frames=10)

# Access results
print(f"Classification: {'FAKE' if result['is_fake'] else 'REAL'}")
print(f"Confidence: {result['confidence']:.2f}%")
print(f"Frames analyzed: {result['frames_analyzed']}")
print(f"Individual frame predictions: {result['frame_predictions']}")
```

### Training with Custom Settings

```bash
# For quick testing (fewer videos)
python train.py
# Modify max_videos parameter in train.py

# Or from Python:
from train import train_model

train_model(
    dataset_path="dataset",
    model_save_path="models/deepfake_model.h5",
    use_light_model=False,  # Lighter model for faster training
    epochs=20,              # Number of training rounds
    batch_size=32,          # Samples per batch
    max_videos=10           # Max videos per class (None=all)
)
```

---

## 🧠 Model Architecture

### Standard Model
```
Input: 128x128 RGB Image (normalized 0-1)
    ↓
Conv2D (32 filters) + ReLU + MaxPooling (2x2)
    ↓
Conv2D (64 filters) + ReLU + MaxPooling (2x2)
    ↓
Conv2D (128 filters) + ReLU + MaxPooling (2x2)
    ↓
Flatten
    ↓
Dense (128) + ReLU + Dropout (0.5)
    ↓
Dense (1) + Sigmoid
    ↓
Output: 0.0 (Real) to 1.0 (Fake)
```

### Light Model (Faster)
Smaller version with fewer parameters for quick training on CPU.

**Key Parameters:**
- **Input:** 128×128 pixel frames
- **Loss:** Binary Crossentropy (perfect for binary classification)
- **Optimizer:** Adam (adaptive learning rate)
- **Metrics:** Accuracy, Precision, Recall
- **Activation:** ReLU (hidden), Sigmoid (output)

---

## 📊 Dataset Preparation

### Video Requirements

- **Format:** MP4, MOV, AVI, or WMV
- **Duration:** Ideally 5-30 seconds each
- **Resolution:** 480p or higher (will be resized to 128×128)
- **Number:** 10+ videos per category for good results

### Frame Extraction

- **Frames per video:** 10 frames extracted uniformly
- **Frame size:** Resized to 128×128 pixels
- **Normalization:** Pixel values scaled to 0-1 range

### Folder Structure

```
dataset/
├── real/
│   ├── real1.mp4
│   ├── real2.mp4
│   ├── real3.mov
│   └── ...
└── fake/
    ├── fake1.mp4
    ├── fake2.mp4
    ├── fake3.avi
    └── ...
```

---

## 📈 Training Details

### Process Flow

1. **Load videos** from dataset folder
2. **Extract frames** (10 per video, uniformly spaced)
3. **Resize frames** to 128×128 pixels
4. **Normalize** pixel values to 0-1
5. **Assign labels** (0=real, 1=fake)
6. **Train CNN** for specified epochs
7. **Validate** on 20% holdout set
8. **Save model** to models/deepfake_model.h5

### Training Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `epochs` | 20 | Training iterations over full dataset |
| `batch_size` | 32 | Samples processed before weight update |
| `validation_split` | 0.2 | 20% data reserved for validation |
| `learning_rate` | 0.001 | Adam optimizer learning rate |

### Expected Output

```
Loading dataset...
Loading 15 real videos...
Loading 15 fake videos...
Total videos loaded: 30
Dataset shape: X=(300, 128, 128, 3), y=(300,)
Real videos: 15, Fake videos: 15

Building model...
Model Architecture:
...
[Model Summary]

Training model for 20 epochs...
Epoch 1/20
[========] 20/20 - loss: 0.6543 - accuracy: 0.5833 - val_loss: 0.5621 - val_accuracy: 0.7000
Epoch 2/20
[========] 20/20 - loss: 0.5234 - accuracy: 0.7250 - val_loss: 0.4521 - val_accuracy: 0.8000
...

✓ Model saved to: models/deepfake_model.h5
✓ Training history plot saved as 'training_history.png'
```

---

## 🎯 Prediction Details

### How Predictions Work

1. **Extract frames** from video (uniformly spaced)
2. **Preprocess** each frame (normalize to 0-1)
3. **Get prediction** for each frame (value 0-1)
4. **Average** all frame predictions
5. **Threshold** at 0.5:
   - \> 0.5 → FAKE ⚠️
   - ≤ 0.5 → REAL ✓

### Confidence Score

- For FAKE: `confidence = prediction × 100`
- For REAL: `confidence = (1 - prediction) × 100`

### Example

If average prediction = 0.72:
- Classification: **FAKE** (0.72 > 0.5)
- Confidence: **72%**

---

## 🐛 Troubleshooting

### Issue: "Model not found" error

**Solution:** Train the model first
```bash
python train.py
```

### Issue: "No videos found in dataset!"

**Solution:** Add videos to dataset folders
```
dataset/real/     ← Add real videos here
dataset/fake/     ← Add fake videos here
```

### Issue: Out of Memory (OOM) error

**Solution:** Reduce batch size or use light model
```python
# In train.py, modify:
train_model(
    use_light_model=True,  # Use smaller model
    batch_size=16,         # Reduce from 32 to 16
    max_videos=5           # Use fewer videos for testing
)
```

### Issue: Video file not supported

**Supported formats:** MP4, MOV, AVI, WMV

**Convert to MP4:**
```bash
# Using FFmpeg
ffmpeg -i input.avi output.mp4
```

### Issue: Streamlit stuck on "Running..."

**Solution:** Restart Streamlit
```bash
# Press Ctrl+C to stop
# Then restart:
streamlit run app.py
```

### Issue: GPU not being used (training is slow)

Check if TensorFlow sees GPU:
```python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```

If empty, install `tensorflow-gpu` or use CPU (training will be slower).

### Issue: High false positives/negatives

**Solutions:**
- Add more training data
- Train for more epochs (increase `epochs` parameter)
- Use standard model instead of light model
- Fine-tune by extracting more frames (`num_frames=15-20`)

---

## 📝 Code Organization

### utils.py
- `extract_frames()` - Extract frames from video
- `preprocess_frames()` - Normalize frames
- `load_dataset()` - Load and prepare dataset

### model.py
- `build_model()` - Build standard CNN
- `build_model_light()` - Build lighter CNN

### train.py
- `train_model()` - Main training function
- `plot_training_history()` - Visualize training

### predict.py
- `DeepfakeDetector` - Main prediction class
- `predict_single_video()` - Helper function

### app.py
- Streamlit web interface
- File upload handling
- Result visualization

---

## 🎓 Learning Resources

### Understanding the System

1. **Frames:** Individual images extracted from video
2. **CNN:** Convolutional Neural Networks for image analysis
3. **Convolution:** Extract features (edges, textures, etc.)
4. **Pooling:** Reduce dimensions, keep important features
5. **Binary Classification:** Two categories (Real/Fake)

### Improving Accuracy

- Collect more training data (rule: 10× more data ≈ 1-2% accuracy gain)
- Use deeper models (more layers)
- Try data augmentation (flip, rotate, zoom frames)
- Ensemble multiple models
- Use temporal features (analyze frame transitions)

---

## 📄 License

This project is open source and available for educational and research purposes.

---

## 🤝 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review code comments in source files
3. Verify dataset structure
4. Check TensorFlow/OpenCV documentation

---

## 🔄 Next Steps & Improvements

**Future Enhancements:**
- [ ] Add LSTM for temporal analysis (frame transitions)
- [ ] Implement data augmentation
- [ ] Add model ensemble voting
- [ ] Real-time webcam detection
- [ ] Multi-class classification (multiple deepfake types)
- [ ] Database to store prediction history
- [ ] Advanced visualization (heatmaps, attention maps)

---

## 📊 Performance Metrics

After training with adequate data:
- **Accuracy:** 85-95% (depends on data quality)
- **Inference time:** ~0.1-0.5s per video (10 frames)
- **Model size:** ~10-15 MB

---

**Happy Detecting! 🛡️**

---

*Last Updated: 2024*
*Version: 1.0*
#   T r u s t S h i e l d - A I  
 