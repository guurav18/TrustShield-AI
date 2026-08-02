# 📋 Complete File Reference

Comprehensive guide to every file in the TrustShield AI project.

---

## 🗂️ File Structure & Descriptions

### 📖 DOCUMENTATION FILES (Start Here!)

#### **START_HERE.md** ⭐ **READ THIS FIRST**
- **Purpose:** Main entry point and navigation guide
- **What it covers:** Quick start, documentation map, learning paths
- **For whom:** Everyone (absolute beginners to developers)
- **Time to read:** 3 minutes
- **Next:** Choose a path based on your needs

#### **QUICKSTART.md**
- **Purpose:** 5-minute setup guide
- **What it covers:** Minimal steps to get running
- **For whom:** People who want immediate results
- **Time to read:** 5 minutes
- **Next:** Follow the 6 steps to get working

#### **README.md**
- **Purpose:** Complete project documentation
- **What it covers:** Everything (85+ sections)
  - Features, requirements, installation
  - How to use, model architecture
  - Training details, prediction guide
  - Troubleshooting, advanced topics
- **For whom:** Developers wanting deep understanding
- **Time to read:** 30 minutes
- **Next:** Refer back as needed

#### **WINDOWS_SETUP.md**
- **Purpose:** Windows-specific installation guide
- **What it covers:**
  - Step-by-step PowerShell commands
  - Common Windows errors and fixes
  - Virtual environment setup
  - Troubleshooting Windows issues
- **For whom:** Windows users having setup issues
- **Time to read:** 15 minutes
- **Next:** Follow Method 1 or 2 exactly

#### **DATASET_GUIDE.md**
- **Purpose:** How to collect and prepare training data
- **What it covers:**
  - Where to find real and fake videos
  - Video requirements and formats
  - Data collection tips
  - Video format conversion
  - Ethical guidelines
  - Dataset optimization
- **For whom:** Anyone collecting training data
- **Time to read:** 20 minutes
- **Next:** Follow to collect your videos

#### **PROJECT_SUMMARY.md**
- **Purpose:** Technical project overview
- **What it covers:**
  - Project structure overview
  - Model architecture details
  - System features and performance
  - How the system works
  - Customization options
  - Code examples
- **For whom:** Developers wanting technical details
- **Time to read:** 15 minutes
- **Next:** Review before customizing

---

### 🧠 CORE CODE FILES

#### **utils.py**
- **Purpose:** Data preprocessing and frame extraction
- **Main functions:**
  - `extract_frames()` - Extract frames from video
  - `preprocess_frames()` - Normalize frames
  - `load_dataset()` - Load entire dataset
  - `prepare_frames_for_prediction()` - Prep frames
- **When to use:** Data loading and preprocessing
- **When to modify:** Adding custom frame extraction logic
- **Size:** ~200 lines

#### **model.py**
- **Purpose:** CNN architecture definitions
- **Main functions:**
  - `build_model()` - Standard CNN model
  - `build_model_light()` - Lightweight CNN
- **When to use:** Building and training models
- **When to modify:** Changing network architecture
- **Size:** ~80 lines

#### **train.py**
- **Purpose:** Model training pipeline
- **Main functions:**
  - `train_model()` - Complete training workflow
  - `plot_training_history()` - Visualize training
- **When to use:** Training the model
- **When to modify:** Changing training parameters
- **How to run:** `python train.py`
- **Size:** ~130 lines

#### **predict.py**
- **Purpose:** Prediction module and inference
- **Main classes:**
  - `DeepfakeDetector` - Main prediction class
- **Main methods:**
  - `predict_video()` - Predict on video
  - `predict_frame()` - Predict single frame
  - `predict_video_verbose()` - Detailed output
- **When to use:** Making predictions
- **When to modify:** Changing prediction logic
- **Size:** ~150 lines

#### **app.py**
- **Purpose:** Streamlit web interface
- **Features:**
  - Video upload
  - Real-time processing
  - Results visualization
  - Frame-by-frame analysis
  - Professional UI
- **When to use:** Web-based video analysis
- **When to modify:** Changing UI or colors
- **How to run:** `streamlit run app.py`
- **Size:** ~200 lines

---

### ⚙️ CONFIGURATION & UTILITIES

#### **config.py**
- **Purpose:** Centralized configuration file
- **What it contains:**
  - Dataset paths
  - Frame extraction settings
  - Model parameters
  - Training settings
  - Prediction settings
  - Streamlit UI settings
- **When to use:** Customizing system behavior
- **When to modify:** Tuning hyperparameters
- **Size:** ~110 lines

#### **verify_setup.py**
- **Purpose:** Installation verification script
- **What it checks:**
  - Python version
  - Required files
  - Directory structure
  - Installed packages
  - Dataset status
- **How to run:** `python verify_setup.py`
- **When to use:** After installation, to verify setup
- **Size:** ~100 lines

#### **examples.py**
- **Purpose:** Usage examples and demonstrations
- **Examples included:**
  1. Verify setup
  2. Load dataset
  3. Extract frames
  4. Train model
  5. Predict single video
  6. Batch prediction
- **How to run:** `python examples.py`
- **When to use:** Learning system usage patterns
- **Size:** ~250 lines

---

### 📁 DIRECTORIES

#### **dataset/**
- **Purpose:** Training data storage
- **Structure:**
  ```
  dataset/
  ├── real/      - Real/authentic videos
  └── fake/      - Deepfake videos
  ```
- **Action:** Add your training videos here
- **Requirements:** 
  - Minimum: 5 videos per category
  - Recommended: 20-50 videos per category
  - Formats: MP4, MOV, AVI, WMV

#### **models/**
- **Purpose:** Trained model storage
- **Contents after training:**
  - `deepfake_model.h5` - Main trained model
- **Size:** ~10-15 MB per model
- **Backups:** Keep old models for comparison

---

### 📦 PROJECT FILES

#### **requirements.txt**
- **Purpose:** Python dependency specifications
- **Contents:** List of all required packages with versions
- **How to use:** `pip install -r requirements.txt`
- **When to modify:** Adding new dependencies
- **Packages included:**
  - numpy, pandas
  - opencv-python
  - tensorflow, keras
  - matplotlib
  - streamlit
  - Pillow

#### **.gitignore**
- **Purpose:** Git configuration to exclude certain files
- **What it excludes:**
  - Virtual environment (`venv/`)
  - Cached files (`__pycache__/`)
  - Video files (`*.mp4`, `*.avi`, etc.)
  - Model files (`*.h5`)
  - Temporary files
- **When to modify:** If adding new file types to ignore

---

## 🗺️ DOCUMENTATION MAP

```
START_HERE.md (Main Entry Point)
    │
    ├─→ QUICKSTART.md ........... (5 min setup)
    │
    ├─→ WINDOWS_SETUP.md ........ (Windows help)
    │
    ├─→ DATASET_GUIDE.md ........ (Data collection)
    │
    ├─→ README.md ............... (Complete guide)
    │
    └─→ PROJECT_SUMMARY.md ...... (Technical details)
```

---

## 🎯 FILE USAGE GUIDE

### For Different Tasks

#### Task: "Get started (5 minutes)"
→ Read: START_HERE.md, QUICKSTART.md

#### Task: "Collect training data"
→ Read: DATASET_GUIDE.md
→ Organize videos in: `dataset/real/` and `dataset/fake/`

#### Task: "Train the model"
→ Run: `python train.py`
→ Modify (if needed): `config.py` or `train.py`

#### Task: "Analyze videos"
→ Run: `streamlit run app.py`
→ Upload videos in web interface

#### Task: "Make predictions in code"
→ Use: `predict.py`
→ Reference: `examples.py`

#### Task: "Customize system"
→ Edit: `config.py` (easy) or `model.py` (advanced)
→ Reference: PROJECT_SUMMARY.md

#### Task: "Troubleshoot issues"
→ Run: `python verify_setup.py`
→ Check: WINDOWS_SETUP.md or README.md

#### Task: "Understand the code"
→ Read: PROJECT_SUMMARY.md "Key Code Examples"
→ Study: Source files with comments
→ Run: `python examples.py`

---

## 📊 FILE STATISTICS

### Code Files
| File | Lines | Purpose |
|------|-------|---------|
| utils.py | ~200 | Data processing |
| model.py | ~80 | Architecture |
| train.py | ~130 | Training |
| predict.py | ~150 | Prediction |
| app.py | ~200 | Web UI |
| config.py | ~110 | Configuration |
| examples.py | ~250 | Examples |
| verify_setup.py | ~100 | Verification |
| **Total** | **~1,220** | **All code** |

### Documentation Files
| File | Pages | Purpose |
|------|-------|---------|
| START_HERE.md | ~5 | Navigation |
| QUICKSTART.md | ~3 | Quick setup |
| WINDOWS_SETUP.md | ~4 | Windows guide |
| DATASET_GUIDE.md | ~8 | Data collection |
| README.md | ~20 | Complete guide |
| PROJECT_SUMMARY.md | ~12 | Technical overview |
| **Total** | **~52** | **All docs** |

---

## 🔄 Recommended Reading Order

### For Absolute Beginners
1. START_HERE.md (3 min)
2. QUICKSTART.md (5 min)
3. DATASET_GUIDE.md (20 min)
4. Follow setup steps
5. Collect data
6. Train and run!

### For Experienced Developers
1. START_HERE.md (skim)
2. PROJECT_SUMMARY.md (15 min)
3. Review source files
4. Modify config.py as needed
5. Run and deploy!

### For Those Customizing
1. START_HERE.md
2. PROJECT_SUMMARY.md
3. config.py (read all options)
4. model.py (understand architecture)
5. Modify and test!

---

## 🎨 Color-Coded Usage

### 🟢 Green (Must Read First)
- START_HERE.md
- QUICKSTART.md

### 🟡 Yellow (Read When Needed)
- WINDOWS_SETUP.md
- DATASET_GUIDE.md
- README.md

### 🔵 Blue (Reference)
- PROJECT_SUMMARY.md
- Source code comments
- examples.py

### 🔴 Red (Advanced)
- Modifying architecture
- GPU setup
- Custom training

---

## ✅ Pre-Execution Checklist

Before running code:
1. [ ] Read START_HERE.md
2. [ ] Run: `python verify_setup.py`
3. [ ] Check: All packages installed
4. [ ] Add: Videos to dataset folders
5. [ ] Review: config.py settings

---

## 🚀 Quick Reference Commands

```bash
# Install
pip install -r requirements.txt

# Verify
python verify_setup.py

# See examples
python examples.py

# Train model
python train.py

# Run web app
streamlit run app.py
```

---

## 📞 File Relationships

```
START_HERE.md (Entry Point)
    ↓
    ├→ utils.py (Data loading)
    │   ↓
    ├→ model.py (Architecture)
    │   ↓
    ├→ train.py (Uses utils + model)
    │   ↓
    ├→ predict.py (Uses model + utils)
    │   ↓
    └→ app.py (Uses predict + config)
        ↓
        └→ config.py (Settings for all)
            ↑
            └→ verify_setup.py (Checks all)
```

---

## 💾 File Sizes (Approximate)

| File Type | Total Size |
|-----------|-----------|
| Source code (.py files) | ~100 KB |
| Documentation (.md files) | ~200 KB |
| Dataset (50 videos) | ~5-10 GB |
| Trained model (.h5) | ~10-15 MB |
| Python packages | ~1-2 GB |

---

## 🎯 Next Steps

1. **Read:** START_HERE.md
2. **Choose:** A learning path
3. **Collect:** Training data using DATASET_GUIDE.md
4. **Train:** Using train.py
5. **Deploy:** Using streamlit run app.py
6. **Customize:** Using config.py and source files

---

## 🆘 Quick Problem Solver

| Problem | Solution File |
|---------|---------------|
| Setup issues | WINDOWS_SETUP.md |
| Installation fails | README.md (Troubleshooting) |
| No data | DATASET_GUIDE.md |
| Model not training | config.py (Check settings) |
| Web app crashes | examples.py (Check usage) |
| Want customization | PROJECT_SUMMARY.md |

---

**Version:** 1.0  
**Last Updated:** April 2024  
**Status:** Complete ✓

---

**Everything you need is here. Let's build! 🛡️**
