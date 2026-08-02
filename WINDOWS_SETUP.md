# 🪟 Windows Installation Guide

Complete step-by-step guide for setting up TrustShield AI on Windows.

---

## Prerequisites

- **Windows 10/11**
- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
  - ⚠️ During installation, **CHECK** "Add Python to PATH"
- **At least 4GB RAM** (8GB recommended)
- **2GB free disk space** (excluding videos)

---

## Method 1: Quick Installation (PowerShell)

### Step 1: Open PowerShell
- Press `Win + R`
- Type `powershell` and press Enter
- Or search for "PowerShell" in Start menu

### Step 2: Navigate to Project Folder
```powershell
cd "C:\Users\Gaurav\OneDrive\文档\Desktop\deepfake"
```

### Step 3: Create Virtual Environment
```powershell
python -m venv venv
```

### Step 4: Activate Virtual Environment
```powershell
venv\Scripts\activate
```

You should see `(venv)` at the beginning of the command line.

### Step 5: Install Dependencies
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

**Note:** This may take 5-10 minutes on first run.

### Step 6: Verify Installation
```powershell
python verify_setup.py
```

Expected output:
```
✓ Python 3.8+ found
✓ All required files present
✓ All packages installed
✓ All checks passed! System is ready.
```

---

## Method 2: Manual Installation (GUI)

### Step 1: Open File Explorer
- Navigate to: `C:\Users\Gaurav\OneDrive\文档\Desktop\deepfake`

### Step 2: Create Virtual Environment
- Open PowerShell in this folder (Shift + Right-click → Open PowerShell here)
- Run: `python -m venv venv`

### Step 3: Activate Virtual Environment
- In PowerShell: `venv\Scripts\activate`

### Step 4: Install Packages
```powershell
pip install -r requirements.txt
```

---

## Troubleshooting Windows Installation

### Problem: "Python is not recognized"
**Solution:**
1. Reinstall Python from [python.org](https://www.python.org/downloads/)
2. **Important:** Check "Add Python to PATH" during installation
3. Restart PowerShell after installation

### Problem: "pip is not recognized"
**Solution:**
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Problem: "Permission denied" error
**Solution:**
1. Run PowerShell as Administrator (Right-click → Run as administrator)
2. Try again: `pip install -r requirements.txt`

### Problem: Installation hangs/very slow
**Solution:**
```powershell
pip install --default-timeout=1000 -r requirements.txt
```

### Problem: "venv\Scripts\activate" doesn't work
**Solution:** Use this instead:
```powershell
.\venv\Scripts\Activate.ps1
```

If you get a "cannot be loaded because running scripts is disabled" error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

---

## Next Steps

### 1. Prepare Training Data
```
dataset/
├── real/     ← Add real videos here (.mp4, .avi, .mov, .wmv)
└── fake/     ← Add deepfake videos here
```

### 2. Train Model
```powershell
python train.py
```

### 3. Run Web Interface
```powershell
streamlit run app.py
```

Opens automatically at: `http://localhost:8501`

---

## GPU Support (Optional - for faster training)

If you have an NVIDIA GPU:

```powershell
# Uninstall default TensorFlow
pip uninstall tensorflow -y

# Install GPU version
pip install tensorflow-gpu==2.13.0
```

Check if GPU is detected:
```powershell
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

---

## PowerShell Tips

- **Copy text:** Right-click in PowerShell (Ctrl+C might not work)
- **Paste text:** Right-click in PowerShell (Ctrl+V might not work)
- **Clear screen:** `cls`
- **List files:** `dir`
- **Change folder:** `cd folder_name`
- **Exit virtual environment:** `deactivate`

---

## Common Windows-Specific Issues

### Issue: Long file paths
Windows has a 260-character limit for file paths.
**Solution:** Enable long paths:
```powershell
# Run as Administrator
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

### Issue: Special characters in path
The path contains Chinese characters (文档). This is usually fine, but if you encounter issues:
**Solution:** Create project in a simpler path:
```powershell
cd C:\Users\Gaurav\Desktop\deepfake
```

### Issue: Antivirus blocks installation
**Solution:**
- Temporarily disable antivirus during installation
- Or add Python folder to antivirus whitelist

---

## Video Converter (for format conversion)

If your videos aren't MP4:

**Using FFmpeg:**
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Install it
3. Convert videos:
```powershell
ffmpeg -i input.avi output.mp4
```

**Or use online converter:**
- https://www.online-convert.com/ (free)
- https://convertio.co/ (free)

---

## Next Section: Training Data Collection

See [Dataset Guide](DATASET_GUIDE.md) for information on:
- Where to find videos
- How many videos needed
- Video format requirements
- Ethical considerations

---

## Getting Help

If you're still having issues:
1. Check [README.md](README.md) troubleshooting section
2. Run `python verify_setup.py` to diagnose problems
3. Check error messages carefully - they usually explain the solution

---

**You're all set! Proceed to:** [QUICKSTART.md](QUICKSTART.md)
