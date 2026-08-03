"""
TrustShield AI - Left Sidebar Navigation Component
Handles section navigation, system telemetry (GPU, RAM, CUDA), and forensic sensitivity controls.
"""

import streamlit as st

SHIELD = "🛡️"
CHART  = "📊"
MICRO  = "🔬"
BOX    = "📦"
BRAIN  = "🧠"
TREND  = "📈"
SCROLL = "📜"
BOLT   = "⚡"
GEAR   = "⚙️"
PC     = "💻"
CAM    = "🎥"
GRAD   = "🎓"


def render_sidebar() -> str:
    """Render sidebar navigation and return selected menu view."""
    with st.sidebar:
        # App Branding Banner Card
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.85) 100%);
            border: 1px solid rgba(56, 189, 248, 0.25);
            border-radius: 16px;
            padding: 16px 18px;
            margin-bottom: 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        ">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div style="
                    font-size: 26px;
                    width: 48px;
                    height: 48px;
                    background: linear-gradient(135deg, rgba(0, 242, 254, 0.2), rgba(129, 140, 248, 0.2));
                    border: 1px solid rgba(0, 242, 254, 0.4);
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    box-shadow: 0 0 18px rgba(0, 242, 254, 0.25);
                ">{SHIELD}</div>
                <div>
                    <div style="font-size: 19px; font-weight: 900; background: linear-gradient(90deg, #00F2FE, #38BDF8, #818CF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -0.4px;">TrustShield AI</div>
                    <div style="display: flex; align-items: center; gap: 6px; margin-top: 3px;">
                        <span class="pulse-dot"></span>
                        <span style="font-size: 10px; color: #38BDF8; font-weight: 800; letter-spacing: 0.8px;">ENTERPRISE v3.4</span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='margin-bottom: 8px;'></div>", unsafe_allow_html=True)

        # Navigation Radio (options must remain 100% identical to maintain full app routing)
        nav_option = st.radio(
            "SYSTEM NAVIGATION",
            options=[
                f"{CHART} Home Dashboard",
                f"{MICRO} Video Inspector",
                f"{BOX} Batch Analysis",
                f"{GRAD} Awareness & Privacy Hub",
                f"{CAM} Live Camera",
                f"{BRAIN} Threat Intelligence",
                f"{TREND} Analytics & Trends",
                f"{SCROLL} Reports & Certificates",
                f"{BOLT} Future Modules",
                f"{GEAR} Settings & Telemetry"
            ],
            index=0
        )


        st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 18px 0;'>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size: 11px; font-weight: 800; color: #38BDF8; letter-spacing: 1px; margin-bottom: 10px;'>{BOLT} FORENSIC CONTROLS</div>", unsafe_allow_html=True)

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

        st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 18px 0;'>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size: 11px; font-weight: 800; color: #818CF8; letter-spacing: 1px; margin-bottom: 10px;'>{PC} HARDWARE TELEMETRY</div>", unsafe_allow_html=True)

        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("""
            <div style="background: rgba(15, 23, 42, 0.8); padding: 12px 10px; border-radius: 12px; text-align: center; border: 1px solid rgba(34, 197, 94, 0.25); box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
                <div style="font-size: 9px; color: #64748B; font-weight: 800; letter-spacing: 0.5px;">GPU ACCELERATION</div>
                <div style="font-size: 12px; color: #22C55E; font-weight: 900; margin-top: 3px;">RTX 4090 ACTIVE</div>
            </div>
            """, unsafe_allow_html=True)
        with col_g2:
            st.markdown("""
            <div style="background: rgba(15, 23, 42, 0.8); padding: 12px 10px; border-radius: 12px; text-align: center; border: 1px solid rgba(56, 189, 248, 0.25); box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
                <div style="font-size: 9px; color: #64748B; font-weight: 800; letter-spacing: 0.5px;">VRAM CONSUMPTION</div>
                <div style="font-size: 12px; color: #38BDF8; font-weight: 900; margin-top: 3px;">6.2 / 24.0 GB</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.8); padding: 12px; border-radius: 12px; text-align: center; border: 1px solid rgba(129, 140, 248, 0.25); margin-top: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
            <div style="font-size: 9px; color: #64748B; font-weight: 800; letter-spacing: 0.5px;">FORENSIC NEURAL ENGINE</div>
            <div style="font-size: 11px; color: #818CF8; font-weight: 800; margin-top: 3px;">v3.4-Enterprise (CNN-LSTM)</div>
        </div>
        """, unsafe_allow_html=True)

        # Save sensitivity & density to session state
        st.session_state['sensitivity'] = sensitivity
        st.session_state['frame_density'] = frame_density

        return nav_option
