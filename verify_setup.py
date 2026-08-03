"""
Quick test script to verify TrustShield AI installation
Run this to check if everything is set up correctly
"""

import sys
import os
from pathlib import Path

# Configure stdout encoding for Windows compatibility
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Fallback symbols if encoding fails
try:
    print("\u2713", end="")
    print("\r", end="")
    OK_SYM = "✓"
    ERR_SYM = "✗"
    WARN_SYM = "⚠"
except UnicodeEncodeError:
    OK_SYM = "[OK]"
    ERR_SYM = "[X]"
    WARN_SYM = "[!]"

print("\n" + "="*60)
print("TrustShield AI - Installation Verification")
print("="*60 + "\n")

# Check Python version
print("1. Checking Python version...")
python_version = sys.version_info
if python_version.major == 3 and python_version.minor >= 8:
    print(f"   {OK_SYM} Python {python_version.major}.{python_version.minor} found")
else:
    print(f"   {ERR_SYM} Python 3.8+ required (found {python_version.major}.{python_version.minor})")

# Check required files
print("\n2. Checking project structure...")
required_files = [
    "utils.py",
    "model.py",
    "train.py",
    "predict.py",
    "app.py",
    "requirements.txt"
]

all_files_exist = True
for file in required_files:
    if os.path.exists(file):
        print(f"   {OK_SYM} {file}")
    else:
        print(f"   {ERR_SYM} {file} NOT FOUND")
        all_files_exist = False

if not all_files_exist:
    print("\n   ERROR: Some required files are missing!")
    sys.exit(1)

# Check directories
print("\n3. Checking directories...")
required_dirs = [
    "dataset",
    "dataset/real",
    "dataset/fake",
    "models"
]

for dir_path in required_dirs:
    if os.path.exists(dir_path):
        print(f"   {OK_SYM} {dir_path}/")
    else:
        print(f"   {ERR_SYM} {dir_path}/ NOT FOUND")

# Try importing required packages
print("\n4. Checking Python packages...")
packages = {
    'numpy': 'NumPy',
    'cv2': 'OpenCV',
    'tensorflow': 'TensorFlow',
    'keras': 'Keras',
    'matplotlib': 'Matplotlib',
    'plotly': 'Plotly',
    'streamlit': 'Streamlit',
    'PIL': 'Pillow'
}

all_packages_installed = True
for package, name in packages.items():
    try:
        __import__(package)
        print(f"   {OK_SYM} {name}")
    except ImportError:
        print(f"   {ERR_SYM} {name} NOT INSTALLED")
        all_packages_installed = False

if not all_packages_installed:
    print("\n   ERROR: Some packages are not installed!")
    print("   Run: pip install -r requirements.txt")
    sys.exit(1)

# Check if model exists
print("\n5. Checking trained model...")
if os.path.exists("models/deepfake_model.h5"):
    print(f"   {OK_SYM} Model found (models/deepfake_model.h5)")
else:
    print(f"   {WARN_SYM} Model not found - you need to train first")
    print("     Run: python train.py")

# Check dataset
print("\n6. Checking dataset...")
real_videos = list(Path("dataset/real").glob("*.*"))
fake_videos = list(Path("dataset/fake").glob("*.*"))

print(f"   Real videos: {len(real_videos)}")
print(f"   Fake videos: {len(fake_videos)}")

if len(real_videos) == 0 or len(fake_videos) == 0:
    print(f"\n   {WARN_SYM} Dataset incomplete - add videos to dataset/real and dataset/fake")

# Final summary
print("\n" + "="*60)
if all_files_exist and all_packages_installed:
    print(f"{OK_SYM} All checks passed! System is ready.")
    print("\nNext steps:")
    print("1. Add training videos to dataset/real and dataset/fake")
    print("2. Run: python train.py")
    print("3. Run: streamlit run app.py")
else:
    print(f"{ERR_SYM} Some checks failed. Please fix issues above.")
    sys.exit(1)

print("="*60 + "\n")

