"""
TrustShield AI - Enterprise Multi-Modal Deepfake Forensic Intelligence Platform
Main Entry Point
"""

import streamlit as st
import os
from predict import DeepfakeDetector

# Page configuration
st.set_page_config(
    page_title="TrustShield AI - Enterprise Multi-Modal Deepfake Intelligence Platform",
    page_icon="🛡️",
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
    except Exception as e:
        return DeepfakeDetector(None)

detector = load_detector()

# Import Modular View Components
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.single_inspector import render_single_inspector
from components.batch_analysis import render_batch_analysis
from components.analytics_dashboard import render_analytics_dashboard
from components.threat_intelligence import render_threat_intelligence
from components.future_modules import render_future_modules
from components.report_certificate import render_reports_page

# Render Sidebar & Capture View Choice
view_choice = render_sidebar()

# Main Router
if view_choice == "📊 Home Dashboard":
    render_hero()
    render_single_inspector(detector)
elif view_choice == "🔬 Video Inspector":
    render_hero()
    render_single_inspector(detector)
elif view_choice == "📦 Batch Analysis":
    render_batch_analysis(detector)
elif view_choice == "🛡️ Live Camera":
    st.markdown("## 🛡️ Live Camera Shield Simulator")
    render_future_modules()
elif view_choice == "🧠 Threat Intelligence":
    render_threat_intelligence()
elif view_choice == "📈 Analytics & Trends":
    render_analytics_dashboard()
elif view_choice == "📜 Reports & Certificates":
    render_reports_page()
elif view_choice == "⚡ Future Modules":
    render_future_modules()
elif view_choice == "⚙️ Settings & Telemetry":
    st.subheader("⚙️ Enterprise System Settings & Telemetry")
    st.markdown("""
    - **Engine Architecture:** Multi-Modal Spatial-Temporal CNN-LSTM
    - **GradCAM Module:** Active Attention Map Overlay Engine
    - **Proof Standard:** ISO 27037 / C2PA Cryptographic Evidence Specification
    - **Model Checkpoint:** `models/deepfake_model.h5`
    - **Python Environment:** PyTorch / TensorFlow Hybrid Core
    """)
    st.success("✅ TrustShield AI System Operating Normally.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 13px; margin-top: 20px;">
    <p><b>TrustShield AI Enterprise Platform v3.4</b> | Built by <b>Gaurav Gupta</b> 🙌❤️</p>
    <p>🔒 Privacy-First Architecture | Local SHA-256 Evidence Hashing | ISO 27037 & C2PA Specification Compliant</p>
</div>
""", unsafe_allow_html=True)
