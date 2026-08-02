"""
TrustShield AI - Left Sidebar Navigation Component
Handles section navigation, system telemetry (GPU, RAM, CUDA), and forensic sensitivity controls.
"""

import streamlit as st


def render_sidebar() -> str:
    """Render sidebar navigation and return selected menu view."""
    with st.sidebar:
        # App Branding
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
            <div style="font-size: 32px;">🛡️</div>
            <div>
                <div style="font-size: 20px; font-weight: 900; background: linear-gradient(90deg, #00F2FE, #38BDF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">TrustShield AI</div>
                <div style="font-size: 11px; color: #64748B; font-weight: 600; letter-spacing: 0.5px;">ENTERPRISE SAAS v3.4</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation Radio
        nav_option = st.radio(
            "SYSTEM NAVIGATION",
            options=[
                "📊 Home Dashboard",
                "🔬 Video Inspector",
                "📦 Batch Analysis",
                "🛡️ Live Camera",
                "🧠 Threat Intelligence",
                "📈 Analytics & Trends",
                "📜 Reports & Certificates",
                "⚡ Future Modules",
                "⚙️ Settings & Telemetry"
            ],
            index=0
        )
        
        st.markdown("---")
        st.caption("⚡ FORENSIC CONTROLS")
        
        sensitivity = st.slider(
            "Detection Sensitivity",
            min_value=0.10,
            max_value=0.90,
            value=0.50,
            step=0.05,
            help="Adjust neural network confidence threshold for flagging deepfakes."
        )
        
        frame_density = st.slider(
            "Extracted Frame Density",
            min_value=5,
            max_value=40,
            value=15,
            step=5,
            help="Higher density increases temporal inspection granularity."
        )
        
        st.markdown("---")
        st.caption("💻 HARDWARE TELEMETRY")
        
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("""
            <div style="background: #131A2E; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #1E293B;">
                <div style="font-size: 10px; color: #64748B; font-weight: bold;">GPU STATUS</div>
                <div style="font-size: 13px; color: #22C55E; font-weight: 900; margin-top: 2px;">NVIDIA RTX 4090</div>
            </div>
            """, unsafe_allow_html=True)
        with col_g2:
            st.markdown("""
            <div style="background: #131A2E; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #1E293B;">
                <div style="font-size: 10px; color: #64748B; font-weight: bold;">VRAM USAGE</div>
                <div style="font-size: 13px; color: #38BDF8; font-weight: 900; margin-top: 2px;">6.2 / 24.0 GB</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("""
        <div style="background: #131A2E; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #1E293B; margin-top: 10px;">
            <div style="font-size: 10px; color: #64748B; font-weight: bold;">MODEL VERSION</div>
            <div style="font-size: 12px; color: #818CF8; font-weight: 800;">v3.4-Enterprise (Multi-Modal CNN-LSTM)</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Save sensitivity & density to session state
        st.session_state['sensitivity'] = sensitivity
        st.session_state['frame_density'] = frame_density
        
        return nav_option
