# 🚀 Quick Start Guide - TrustShield AI

This guide will get you up and running in 5 minutes.

---

## Step 1: Install Dependencies (2 minutes)

### On Windows:

```powershell
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### On macOS/Linux:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

**Note:** First time installation may take 5-10 minutes.

---

## Step 2: Verify Installation (1 minute)

```bash
python verify_setup.py
```

You should see:
```
✓ Python 3.8+ found
✓ All required files present
✓ All packages installed
```

---

## Step 3: Prepare Training Data (varies)

1. Find or download deepfake and real videos
2. Create folders:
   ```
   dataset/
   ├── real/
   │   ├── video1.mp4
   │   ├── video2.mp4
   │   └── ...
   └── fake/
       ├── deepfake1.mp4
       ├── deepfake2.mp4
       └── ...
   ```

3. Use at least 5 videos per category for good results

**Where to find videos:**
- Real videos: YouTube, TikTok, movies
- Deepfake videos: Academic datasets, YouTube deepfake examples

---

## Step 4: Train the Model (5-30 minutes)

```bash
python train.py
```

You'll see:
```
Loading dataset...
Loading 15 real videos...
Loading 15 fake videos...
Total videos loaded: 30
Dataset shape: X=(300, 128, 128, 3), y=(300,)

Building model...
Training model for 20 epochs...
Epoch 1/20 [...] accuracy: 0.58
Epoch 2/20 [...] accuracy: 0.72
...
✓ Model saved to: models/deepfake_model.h5
```

**Once training is complete**, you'll have `models/deepfake_model.h5`

---

## Step 5: Run the Web Interface (1 minute)

```bash
streamlit run app.py
```

Browser opens automatically at `http://localhost:8501`

You should see:
```
🛡️ TrustShield AI
Deepfake Video Detection System
[Upload Video Button]
```

---

## Step 6: Test with a Video (1 minute)

1. Click **"Choose a video file"**
2. Select an MP4, MOV, AVI, or WMV file
3. Click **"Analyze Video"**
4. See results: **REAL** ✓ or **FAKE** ⚠️

---

## Common Issues & Solutions

### ❌ "Model not found"
→ Run `python train.py` first

### ❌ "No videos found in dataset!"
→ Add videos to `dataset/real` and `dataset/fake`

### ❌ Package installation fails
→ Try: `pip install --upgrade pip`
→ Then: `pip install -r requirements.txt`

### ❌ Out of memory
→ In `train.py`, change: `use_light_model=True`

---

## What Each File Does

| File | Purpose |
|------|---------|
| `utils.py` | Extract frames from videos, preprocess data |
| `model.py` | Define CNN architecture |
| `train.py` | Train the model on your dataset |
| `predict.py` | Make predictions on new videos |
| `app.py` | Streamlit web interface |
| `verify_setup.py` | Check if everything is installed |

---

## Next: Advanced Usage

### Train with custom settings:

```bash
# For quick testing with fewer videos:
# Edit train.py and change max_videos=5

# For faster training with lighter model:
# In train.py: use_light_model=True, epochs=10
```

### Use prediction in your code:

```python
from predict import DeepfakeDetector

detector = DeepfakeDetector("models/deepfake_model.h5")
result = detector.predict_video("my_video.mp4")

print(f"Result: {'FAKE' if result['is_fake'] else 'REAL'}")
print(f"Confidence: {result['confidence']:.1f}%")
```

---

## Performance Tips

✓ **Better accuracy:**
- Add more training videos (50+)
- Train for more epochs (30-50)
- Use standard model (not light)

✓ **Faster training:**
- Use light model
- Reduce epochs to 10
- Use GPU (if available)

✓ **Faster inference:**
- Reduce num_frames to 5
- Use light model

---

## You're Ready! 🎉

Go analyze some videos!

```bash
streamlit run app.py
```

---

**Questions?** Check README.md for detailed documentation.
