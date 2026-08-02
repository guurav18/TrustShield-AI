# 🛡️ TrustShield AI - START HERE

Welcome to TrustShield AI! This guide will help you get started.

---

## ⚡ 5-Minute Quick Start

**Want to get up and running immediately?**

1. **Install:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Verify:**
   ```bash
   python verify_setup.py
   ```

3. **Add Videos:**
   - Put real videos in `dataset/real/`
   - Put deepfake videos in `dataset/fake/`
   - Need at least 5 of each

4. **Train:**
   ```bash
   python train.py
   ```

5. **Run:**
   ```bash
   streamlit run app.py
   ```

Done! 🎉

---

## 📖 Choose Your Path

### 🎯 I'm a Beginner (New to AI/ML)

1. **Read First:** [QUICKSTART.md](QUICKSTART.md) (5 min read)
2. **Then:** [README.md](README.md) - "Understanding the System" section
3. **Then:** Collect data using [DATASET_GUIDE.md](DATASET_GUIDE.md)
4. **Finally:** Run the system

### 🪟 I'm on Windows

Follow [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for step-by-step Windows-specific instructions.

### 👨‍💻 I'm a Developer (Familiar with ML)

1. Review [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
2. Check the code in `utils.py`, `model.py`, `train.py`
3. Modify `config.py` for custom settings
4. Run `python examples.py` to see usage patterns

### 🔧 I Want to Customize

1. Edit `config.py` for settings
2. Edit `model.py` to change architecture
3. Edit `train.py` to modify training logic
4. See [README.md](README.md) "Customization" section

---

## 📚 Documentation Map

```
START HERE (this file)
    ├─ QUICKSTART.md ............. 5-minute setup
    ├─ WINDOWS_SETUP.md .......... Windows installation
    ├─ DATASET_GUIDE.md .......... Data collection
    ├─ README.md ................. Complete documentation
    ├─ PROJECT_SUMMARY.md ........ Project overview
    └─ examples.py ............... Code examples
```

---

## 🎯 What Do You Want to Do?

### "I want to just try it"
→ Read [QUICKSTART.md](QUICKSTART.md) (5 min)

### "I want to understand the system"
→ Read [README.md](README.md) section: "How the System Works"

### "I want to collect training data"
→ Read [DATASET_GUIDE.md](DATASET_GUIDE.md)

### "I want to train a model"
→ Read [QUICKSTART.md](QUICKSTART.md) section: "Step 4: Train the Model"

### "I want to modify the code"
→ Read [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) section: "Key Code Examples"

### "I have an installation error"
→ Read [WINDOWS_SETUP.md](WINDOWS_SETUP.md) or [README.md](README.md) "Troubleshooting"

### "I want code examples"
→ Look at [examples.py](examples.py) or run: `python examples.py`

---

## 📋 System Requirements

- **Python:** 3.8 or higher
- **RAM:** 4GB minimum (8GB recommended)
- **Disk:** 2GB free space (excluding video data)
- **OS:** Windows, macOS, or Linux

**Check your system:**
```bash
python verify_setup.py
```

---

## 🚀 Installation Overview

### Step 1: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # macOS/Linux
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python verify_setup.py
```

**Issues?** Check [WINDOWS_SETUP.md](WINDOWS_SETUP.md) or [README.md](README.md)

---

## 📁 Project Structure at a Glance

```
deepfake/
├── dataset/            ← Add your training videos here
│   ├── real/          ← Authentic videos
│   └── fake/          ← Deepfake videos
├── models/            ← Trained models go here
│
├── Core Code:
│   ├── utils.py       ← Frame extraction
│   ├── model.py       ← CNN architecture  
│   ├── train.py       ← Training script
│   ├── predict.py     ← Prediction module
│   └── app.py         ← Web interface
│
└── Documentation:
    ├── README.md
    ├── QUICKSTART.md
    ├── WINDOWS_SETUP.md
    ├── DATASET_GUIDE.md
    └── PROJECT_SUMMARY.md
```

---

## 🎬 The Process in 3 Steps

### 1️⃣ PREPARE
```
Collect videos
    ↓
Organize in dataset/real/ and dataset/fake/
    ↓
Ready to train!
```

### 2️⃣ TRAIN
```
python train.py
    ↓
CNN learns to detect deepfakes
    ↓
Model saved to models/deepfake_model.h5
```

### 3️⃣ PREDICT
```
streamlit run app.py
    ↓
Upload video
    ↓
Get prediction (REAL or FAKE)
```

---

## 🎯 Key Files & What They Do

| File | Purpose | When You Need It |
|------|---------|------------------|
| `utils.py` | Frame extraction & preprocessing | Understanding data pipeline |
| `model.py` | CNN architecture | Customizing the model |
| `train.py` | Training script | Training the model |
| `predict.py` | Prediction module | Making predictions |
| `app.py` | Web interface | Running the application |
| `config.py` | Settings | Customizing parameters |
| `verify_setup.py` | Installation check | Verifying setup |
| `examples.py` | Code examples | Learning usage patterns |

---

## ⚡ Common Tasks

### Task: "Install Dependencies"
```bash
pip install -r requirements.txt
```

### Task: "Check Installation"
```bash
python verify_setup.py
```

### Task: "Train Model"
```bash
python train.py
```

### Task: "Run Web App"
```bash
streamlit run app.py
```

### Task: "See Examples"
```bash
python examples.py
```

### Task: "Make Predictions (Code)"
```python
from predict import DeepfakeDetector
detector = DeepfakeDetector("models/deepfake_model.h5")
result = detector.predict_video("video.mp4")
print(result['is_fake'], result['confidence'])
```

---

## 📊 Learning Curve

```
Time  │
      │                    
30min │                    ██ Full Understanding
      │                 █████
15min │              ███████
      │           █████████
 5min │        ███████████ Basics
      │     █████████████
      │  ███████████████ Setup
      │ ██████████████
      └────────────────────────────
        Install  Data  Train  Deploy
```

---

## 🆘 Quick Troubleshooting

### "Python not found"
→ Install Python from [python.org](https://www.python.org/downloads)

### "ModuleNotFoundError"
→ Run: `pip install -r requirements.txt`

### "Model not found"
→ Run: `python train.py` first

### "No videos found"
→ Add videos to `dataset/real/` and `dataset/fake/`

### Still stuck?
→ See [README.md](README.md) "Troubleshooting" section

---

## 🎓 Understanding What's Happening

### What is a CNN?
A Convolutional Neural Network (CNN) is a type of AI that learns to recognize patterns in images. Perfect for deepfake detection!

### Why frames?
Videos are made of frames. We extract multiple frames and analyze each one to get a robust prediction.

### Why 128×128?
Smaller size = faster processing. Deepfakes typically have visual artifacts even at low resolution.

### Why average predictions?
Averaging frame predictions is more reliable than predicting on a single frame.

---

## ✅ Verification Checklist

Before starting:
- [ ] Python 3.8+ installed
- [ ] Ran: `python verify_setup.py` ✓
- [ ] Have videos for dataset
- [ ] 2GB free disk space

Before training:
- [ ] At least 5 real videos in `dataset/real/`
- [ ] At least 5 fake videos in `dataset/fake/`
- [ ] All videos in supported format (MP4, MOV, AVI, WMV)

---

## 🚀 Next Steps

### Immediate (Next 5 minutes)
1. [ ] Read [QUICKSTART.md](QUICKSTART.md)
2. [ ] Run `python verify_setup.py`
3. [ ] Install dependencies

### Short Term (Next 30 minutes)
1. [ ] Collect training videos
2. [ ] Run `python train.py`
3. [ ] Run `streamlit run app.py`

### Medium Term (Next 2 hours)
1. [ ] Test predictions on various videos
2. [ ] Check accuracy
3. [ ] Optimize parameters in `config.py`

### Long Term (Next week+)
1. [ ] Add more training data
2. [ ] Retrain for better accuracy
3. [ ] Customize model architecture
4. [ ] Deploy as production service

---

## 🎉 You're Ready!

Everything you need is here. Pick a learning path above and get started!

### Fastest Path (No reading):
```bash
python verify_setup.py
# Add videos to dataset/real and dataset/fake
python train.py
streamlit run app.py
```

### Recommended Path (Learning):
1. Read [QUICKSTART.md](QUICKSTART.md) (5 min)
2. Read [DATASET_GUIDE.md](DATASET_GUIDE.md) (15 min)
3. Follow setup steps
4. Run the system

### Complete Path (Understanding):
1. Read [README.md](README.md) (30 min)
2. Read [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) (15 min)
3. Study code in `utils.py` and `model.py`
4. Run `examples.py` to see patterns
5. Customize and deploy

---

## 📞 Getting Help

### For Setup Issues
→ [WINDOWS_SETUP.md](WINDOWS_SETUP.md) or [README.md](README.md) Troubleshooting

### For Data Questions
→ [DATASET_GUIDE.md](DATASET_GUIDE.md)

### For Code Questions
→ See comments in source files or [examples.py](examples.py)

### For Usage Questions
→ [README.md](README.md)

---

## 📚 All Documentation Files

| Document | Purpose | Read Time |
|----------|---------|-----------|
| This file | Navigation & overview | 3 min |
| QUICKSTART.md | Fast setup | 5 min |
| WINDOWS_SETUP.md | Windows guide | 15 min |
| DATASET_GUIDE.md | Data collection | 20 min |
| README.md | Complete guide | 30 min |
| PROJECT_SUMMARY.md | Technical overview | 15 min |

---

## 🎯 Your Goal

```
You start here ↓
     ↓
Read documentation ↓
     ↓
Install dependencies ↓
     ↓
Collect training data ↓
     ↓
Train model ↓
     ↓
Run web app ↓
     ↓
Analyze videos ↓
     ↓
SUCCESS! 🎉
```

---

## 💡 Pro Tips

✓ Start with the QUICKSTART for fastest setup
✓ Use `verify_setup.py` to check everything
✓ Begin with just 5-10 videos to test the system
✓ Train with small dataset first, then expand
✓ Use light model for quick testing on CPU
✓ GPU training is 5-10x faster (if available)
✓ Save your best trained models

---

## 🚀 Let's Go!

**Pick a path above and get started!**

**Questions?** Check the relevant documentation file.

**Ready to code?** Open `app.py` and `train.py`.

**Let's detect deepfakes! 🛡️**

---

**Version:** 1.0
**Last Updated:** April 2024
**Status:** Production Ready ✓

---

**Next:** Read [QUICKSTART.md](QUICKSTART.md) →
