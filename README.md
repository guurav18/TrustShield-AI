<div align="center">

# 🛡️ TrustShield AI

### Enterprise AI-Powered Digital Forensics & Deepfake Detection Platform

Detect • Analyze • Explain • Investigate

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

**An Explainable AI platform for detecting manipulated videos using Computer Vision, Deep Learning and Digital Forensics techniques.**

</div>

---

# 🚀 Overview

TrustShield AI is a modern AI-powered Digital Forensics Platform designed to detect Deepfake videos using Deep Learning and Computer Vision.

Unlike traditional deepfake detectors that only classify media as **REAL** or **FAKE**, TrustShield AI focuses on forensic investigation by providing visual explanations, confidence analysis, evidence reports, and an interactive dashboard.

The goal of this project is to improve trust in digital media by combining explainable AI with an intuitive investigation workflow.

---

# ✨ Key Features

- 🎥 AI-based Deepfake Video Detection
- 🧠 CNN-based Deep Learning Model
- 📹 Automatic Video Frame Extraction
- 📊 Confidence Score Prediction
- 📄 AI Investigation Report Generator
- 📈 Interactive Analytics Dashboard
- 🖥️ Modern Streamlit User Interface
- ⚡ Fast Frame-Based Prediction
- 📂 Modular Project Architecture
- 🔬 Explainable AI Ready

---

# 🏗️ System Architecture

```text
                    User Uploads Video
                             │
                             ▼
                  Video Preprocessing
                             │
                             ▼
                  Frame Extraction (OpenCV)
                             │
                             ▼
                  Image Preprocessing
                             │
                             ▼
               CNN Deep Learning Model
                             │
                             ▼
                 Confidence Prediction
                             │
                             ▼
               AI Investigation Report
                             │
                             ▼
              Streamlit Interactive Dashboard
```

---

# 🧠 AI Pipeline

```
Video

↓

Frame Extraction

↓

Image Normalization

↓

CNN Model

↓

Prediction

↓

Confidence Score

↓

Forensic Report

↓

Dashboard
```

---

# 📸 Screenshots

## Dashboard

```
screenshots/dashboard.png
```

---

## Video Analysis

```
screenshots/analysis.png
```

---

## AI Investigation Report

```
screenshots/report.png
```

---

# 🛠 Tech Stack

## Programming

- Python

## AI / Deep Learning

- TensorFlow
- Keras

## Computer Vision

- OpenCV

## Data Processing

- NumPy
- Pandas

## Visualization

- Matplotlib
- Plotly

## Frontend

- Streamlit

---

# 📂 Project Structure

```
TrustShield-AI

│── app.py
│── train.py
│── predict.py
│── model.py
│── utils.py
│── pdf_generator.py
│── config.py
│── requirements.txt
│── README.md

├── dataset
│      ├── real
│      └── fake

├── models

├── assets

├── screenshots

└── docs
```

---

# 📦 Installation

Clone Repository

```bash
git clone https://github.com/USERNAME/TrustShield-AI.git

cd TrustShield-AI
```

Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Run Project

Train Model

```bash
python train.py
```

Launch Dashboard

```bash
streamlit run app.py
```

---

# 📊 Dataset

This project is trained using the **FaceForensics++ (C23)** dataset.

Due to GitHub storage limitations, the dataset is **not included** in this repository.

Expected directory structure:

```
dataset/

    real/

    fake/
```

---

# 📈 Model

Current Model

✅ CNN

Future Models

- CNN + LSTM
- EfficientNet
- Vision Transformer
- Hybrid CNN-LSTM

---

# 📊 Performance

| Metric | Value |
|----------|--------|
| Classification | Binary |
| Input Size | 128 × 128 |
| Output | Real / Fake |
| Framework | TensorFlow |
| UI | Streamlit |

---

# 🌟 Unique Features

Unlike traditional Deepfake Detection systems, TrustShield AI focuses on creating a digital investigation platform.

Current Features

- Deepfake Classification
- Confidence Score
- AI Report Generation
- Modern Dashboard

Planned Features

- Explainable AI (Grad-CAM)
- AI Evidence Heatmaps
- Temporal Frame Analysis
- Multi-Modal Detection
- Audio Analysis
- Emotion Consistency
- Deepfake Generator Identification
- Digital Forensics Certificate
- AI Threat Intelligence Dashboard
- Investigation Timeline
- Real-Time Webcam Detection

---

# 🔬 Future Roadmap

- [ ] CNN + LSTM Architecture
- [ ] Explainable AI
- [ ] Grad-CAM
- [ ] Live Camera Detection
- [ ] WhatsApp Video Scanner
- [ ] Browser Extension
- [ ] AI Investigation Timeline
- [ ] Generator Fingerprint Detection
- [ ] Multi-Modal Deepfake Detection
- [ ] Enterprise Dashboard

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve TrustShield AI, feel free to fork this repository and submit a Pull Request.

---

# 📜 License

This project is released under the MIT License.

---

# 👨‍💻 Author

**Gaurav Gupta**

B.Tech Computer Science Engineering

AI • Machine Learning • Computer Vision • Deep Learning

---

<div align="center">

### ⭐ If you found this project useful, don't forget to Star this Repository ⭐

Made with ❤️ using Python, TensorFlow and OpenCV

</div>
