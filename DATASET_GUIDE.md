# 📚 Dataset Guide

Guide for collecting and preparing training data for TrustShield AI.

---

## Dataset Structure

```
dataset/
├── real/
│   ├── real_video_1.mp4
│   ├── real_video_2.mp4
│   ├── real_video_3.avi
│   └── ...
└── fake/
    ├── deepfake_1.mp4
    ├── deepfake_2.mp4
    ├── deepfake_3.mov
    └── ...
```

---

## Video Requirements

| Aspect | Requirement |
|--------|-------------|
| **Format** | MP4, MOV, AVI, WMV |
| **Duration** | 5-30 seconds (ideal) |
| **Resolution** | 480p or higher |
| **Frame rate** | 24+ fps |
| **File size** | < 100 MB per video |
| **Audio** | Optional (ignored by system) |

---

## Minimum Dataset Size

### Quick Testing
- **5 real videos** + **5 fake videos** = 10 total
- Training time: 2-5 minutes
- Accuracy: ~70-75%
- Purpose: Verify system works

### Good Results
- **20 real videos** + **20 fake videos** = 40 total
- Training time: 10-20 minutes
- Accuracy: ~80-90%
- Purpose: Practical use

### Production Quality
- **100+ real videos** + **100+ fake videos** = 200+ total
- Training time: 1-2 hours
- Accuracy: ~92-98%
- Purpose: Deployment

---

## Where to Find Videos

### REAL Videos (Authentic)
- **YouTube:** Search for interviews, news clips, tutorials
- **TED Talks:** https://www.ted.com/talks
- **News sites:** BBC, Reuters, AP News
- **Social Media:** TikTok, Instagram (celebrities/public figures)
- **Webcam:** Record yourself speaking

### DEEPFAKE Videos (Synthetic)
- **FaceForensics Dataset:** https://github.com/ondyari/FaceForensics
  - Academic dataset with deepfakes
- **Deepfake Detection Challenge:** Kaggle competitions
- **YouTube:** Search "deepfake compilation"
- **Research papers:** Often include sample videos

### Balanced Approach
**Goal:** Real and deepfake videos should be similar in:
- Face size in frame
- Lighting conditions
- Video quality
- Resolution
- Similar speakers/people (if possible)

---

## Video Collection Tips

### ✓ GOOD Examples
```
✓ News anchor speaking to camera (clear face, good lighting)
✓ Interview with person speaking (frontal view)
✓ Selfie-style video (close-up of face)
✓ Tutorial with presenter (consistent lighting)
✓ TED talk (professional quality)
```

### ✗ POOR Examples
```
✗ Video where face is too small (< 50 pixels)
✗ Heavily pixelated or low quality
✗ Side-view (profile angle)
✗ Group of people (multiple faces)
✗ Animated/cartoon content
✗ Very dark or very bright (poor lighting)
```

---

## How to Download Videos

### Using YouTube-DL

**Install:**
```bash
pip install yt-dlp
```

**Download single video:**
```bash
yt-dlp -f best -o "dataset/real/%(title)s.mp4" "VIDEO_URL"
```

**Download multiple videos from playlist:**
```bash
yt-dlp -f best -o "dataset/real/%(title)s.mp4" "PLAYLIST_URL"
```

### Using Browser

1. Install extension: **Video DownloadHelper** or **4K Video Downloader**
2. Browse to video
3. Click extension icon and download
4. Move file to appropriate folder

---

## Video Format Conversion

If videos aren't in supported formats:

### Using FFmpeg

**Install FFmpeg:**
- Windows: [ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

**Convert to MP4:**
```bash
ffmpeg -i input.avi output.mp4
ffmpeg -i input.mov output.mp4
```

**Compress if too large:**
```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -c:a aac -b:a 128k output.mp4
```

### Online Converters
- [Online-Convert.com](https://www.online-convert.com/)
- [CloudConvert.com](https://cloudconvert.com/)
- [Convertio.co](https://convertio.co/)

---

## Video Preprocessing

### Trim Video (keep 10-30 seconds)
```bash
ffmpeg -i input.mp4 -ss 00:00:05 -t 00:00:20 output.mp4
```
(Start at 5s, take 20s duration)

### Extract Frames (preview)
```bash
ffmpeg -i input.mp4 -vf fps=2 frame_%04d.jpg
```

### Check Video Info
```bash
ffmpeg -i input.mp4
```

---

## Data Diversity

**Important:** Ensure dataset covers:

### Diversity Factors
- **Gender:** Mix of male and female
- **Ethnicity:** Multiple ethnicities
- **Age:** Range of ages
- **Lighting:** Different lighting conditions
- **Background:** Various backgrounds
- **Clothing:** Different clothing
- **Expression:** Various facial expressions

**Why?** Training on diverse data prevents bias and improves generalization.

---

## Ethical Considerations

⚠️ **Important Guidelines:**

### DO:
✓ Use publicly available videos
✓ Respect copyright laws
✓ Use videos for academic/research purposes
✓ Get permission for private videos
✓ Label data clearly as real/fake

### DON'T:
✗ Create deepfakes for fraud/deception
✗ Violate privacy (private videos without consent)
✗ Spread misinformation
✗ Use for harassment or blackmail
✗ Violate copyright laws

---

## Dataset Preparation Checklist

- [ ] Collect 5-10+ real videos
- [ ] Collect 5-10+ deepfake videos
- [ ] Verify all videos are in supported format (MP4, MOV, AVI, WMV)
- [ ] Check video quality (not too pixelated)
- [ ] Ensure faces are visible and clear
- [ ] Verify video plays correctly
- [ ] Organize in `dataset/real/` and `dataset/fake/`
- [ ] Consider diversity in your dataset

---

## Testing Your Dataset

### 1. Verify Video Loading
```bash
python verify_setup.py
```

Should show:
```
Real videos: 10
Fake videos: 10
```

### 2. Test Frame Extraction
```bash
python -c "from utils import extract_frames; frames = extract_frames('dataset/real/video.mp4', num_frames=5); print(f'Extracted {len(frames)} frames')"
```

### 3. Quick Training Test
```python
# In train.py, set:
max_videos = 2  # Just 2 videos per class
epochs = 5      # Just 5 epochs
use_light_model = True
```

---

## Common Dataset Issues

### Issue: "No videos found in dataset!"
**Solution:** Verify folder structure
```
✓ dataset/real/     (with videos inside)
✓ dataset/fake/     (with videos inside)
```

### Issue: "Error: Cannot open video file"
**Solution:** 
- Verify video file is not corrupted
- Try opening with VLC player
- Convert to MP4 format

### Issue: "No frames extracted"
**Solution:**
- Video might be too short or corrupted
- Try a different video
- Use FFmpeg to verify: `ffmpeg -i video.mp4`

### Issue: Imbalanced classes (50 real, 5 fake)
**Solution:**
- Collect more deepfake videos, OR
- Use fewer real videos to balance

---

## Public Datasets (Pre-collected)

### Available for Download

1. **FaceForensics++ (CVPR2019)**
   - URL: https://github.com/ondyari/FaceForensics
   - Size: ~1TB
   - Content: Real + multiple deepfake methods
   - For: Research/Academic

2. **Deepfake Detection Challenge**
   - URL: https://www.kaggle.com/c/deepfake-detection-challenge
   - Size: ~470GB
   - Content: Labeled real/fake videos
   - For: Competition/Training

3. **WildDeepfake**
   - URL: https://github.com/deepfakeforensics/wild_deepfake
   - Size: ~8GB
   - Content: In-the-wild deepfakes
   - For: Testing

---

## Quick Start with Sample Data

Don't have videos? Quick alternatives:

### Option 1: Screen Recording
```bash
# Record 30-second webcam video
# Windows: Use built-in Camera app or OBS
# macOS: Use QuickTime Player
# Linux: Use SimpleScreenRecorder
```

### Option 2: YouTube Downloads
```bash
# Download from TED Talks
yt-dlp -f best "https://www.ted.com/talks/..."

# Or search for: "deepfake examples" on YouTube
```

### Option 3: Use Pre-built Datasets
- Minimal: 2-3 videos to test system
- Full: Download FaceForensics++ (requires registration)

---

## Dataset Organization Best Practices

### File Naming Convention
```
dataset/real/
  - person1_speaking.mp4
  - person2_interview.mp4
  - news_clip_001.mp4

dataset/fake/
  - deepfake_person1.mp4
  - morphing_attack_01.mp4
  - generative_001.mp4
```

### Metadata (Optional but Helpful)
Create `dataset_info.txt`:
```
Real Videos (10):
- YouTube interviews
- News clips
- TED talks

Fake Videos (10):
- FaceSwap method (5)
- Face2Face method (3)
- Neural Textures (2)

Total: 20 videos
Collection date: 2024-04-22
```

---

## Performance vs Dataset Size

| Videos | Training Time | Expected Accuracy | Use Case |
|--------|:-------------:|:-----------------:|----------|
| 10 | 2-5 min | 70-75% | Testing/Learning |
| 40 | 10-20 min | 80-90% | Good results |
| 100 | 30-60 min | 90-95% | Reliable |
| 500+ | 2-4 hours | 95-98% | Production |

---

## Next Steps

1. **Collect videos** following this guide
2. **Organize** in dataset/real/ and dataset/fake/
3. **Verify** with `python verify_setup.py`
4. **Train** with `python train.py`
5. **Test** with `streamlit run app.py`

---

**Questions about data collection?** See [README.md](README.md) or [QUICKSTART.md](QUICKSTART.md)
