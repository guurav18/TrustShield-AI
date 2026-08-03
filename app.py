# -*- coding: utf-8 -*-
"""
TrustShield AI - Enterprise Multi-Modal Deepfake Forensic Intelligence Platform
Main Entry Point
"""

import streamlit as st
import os
from predict import DeepfakeDetector

# Emoji constants (unicode escapes - immune to encoding issues)
# Emoji constants (unicode escapes - immune to encoding issues)
SHIELD  = "\U0001F6E1\uFE0F"   # 🛡️
CHART   = "\U0001F4CA"         # 📊
MICRO   = "\U0001F52C"         # 🔬
BOX     = "\U0001F4E6"         # 📦
BRAIN   = "\U0001F9E0"         # 🧠
TREND   = "\U0001F4C8"         # 📈
SCROLL  = "\U0001F4DC"         # 📜
BOLT    = "\u26A1"             # ⚡
GEAR    = "\u2699\uFE0F"       # ⚙️
LOCK    = "\U0001F512"         # 🔒
HEART   = "\u2764\uFE0F"       # ❤️
CAM     = "\U0001F3A5"         # 🎥
CHECK   = "\u2705"             # ✅
GRAD    = "\U0001F393"         # 🎓

# Page configuration
st.set_page_config(
    page_title="TrustShield AI - Enterprise Multi-Modal Deepfake Intelligence Platform",
    page_icon=SHIELD,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Custom CSS System
def load_css(css_file_path):
    if os.path.exists(css_file_path):
        with open(css_file_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

# Model Loading
model_path = "models/deepfake_model.h5"
has_model_file = os.path.exists(model_path)

@st.cache_resource
def load_detector():
    try:
        detector = DeepfakeDetector(model_path if has_model_file else None)
        return detector
    except Exception:
        return DeepfakeDetector(None)

detector = load_detector()

# Import Modular View Components
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.home_dashboard import render_home_dashboard
from components.single_inspector import render_single_inspector
from components.batch_analysis import render_batch_analysis
from components.cyber_awareness import render_cyber_awareness
from components.analytics_dashboard import render_analytics_dashboard
from components.threat_intelligence import render_threat_intelligence
from components.future_modules import render_future_modules
from components.report_certificate import render_reports_page

# Render Sidebar & Capture View Choice
view_choice = render_sidebar()

# Main Router — must match sidebar option strings exactly
if view_choice == f"{CHART} Home Dashboard":
    render_home_dashboard()
elif view_choice == f"{MICRO} Video Inspector":
    render_hero()
    render_single_inspector(detector)
elif view_choice == f"{BOX} Batch Analysis":
    render_batch_analysis(detector)
elif view_choice == f"{GRAD} Awareness & Privacy Hub":
    render_cyber_awareness()

elif view_choice == f"{CAM} Live Camera":
    st.markdown(f"## {CAM} Live Camera Shield Simulator")
    render_future_modules()
elif view_choice == f"{BRAIN} Threat Intelligence":
    render_threat_intelligence()
elif view_choice == f"{TREND} Analytics & Trends":
    render_analytics_dashboard()
elif view_choice == f"{SCROLL} Reports & Certificates":
    render_reports_page()
elif view_choice == f"{BOLT} Future Modules":
    render_future_modules()
elif view_choice == f"{GEAR} Settings & Telemetry":
    st.subheader(f"{GEAR} Enterprise System Settings & Telemetry")
    st.markdown("""
    - **Engine Architecture:** Multi-Modal Spatial-Temporal CNN-LSTM
    - **GradCAM Module:** Active Attention Map Overlay Engine
    - **Proof Standard:** ISO 27037 / C2PA Cryptographic Evidence Specification
    - **Model Checkpoint:** `models/deepfake_model.h5`
    - **Python Environment:** PyTorch / TensorFlow Hybrid Core
    """)
    st.success(f"{CHECK} TrustShield AI System Operating Normally.")

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #64748B; font-size: 13px; margin-top: 20px;">
    <p><b>TrustShield AI Enterprise Platform v3.4</b> | Built by <b>Gaurav Gupta</b> {SHIELD}{HEART}</p>
    <p>{LOCK} Privacy-First Architecture &nbsp;|&nbsp; Local SHA-256 Evidence Hashing &nbsp;|&nbsp; ISO 27037 &amp; C2PA Specification Compliant</p>
</div>
""", unsafe_allow_html=True)
