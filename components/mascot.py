"""
TrustShield AI - ShieldBot Interactive Cyber Mascot Assistant Component
Renders an animated 3D Cyber Bot mascot avatar with speech bubble, interactive tips, and voice greetings.
"""

import streamlit as st
import os
import base64


def render_mascot_widget():
    """Render 3D Cyber Bot Mascot Avatar with speech bubble and interactive cyber security tips."""
    
    # Encode mascot image if available
    mascot_img_html = '<div style="font-size: 64px; text-shadow: 0 0 20px #00F2FE;">🤖</div>'
    if os.path.exists("assets/mascot.png"):
        with open("assets/mascot.png", "rb") as img_file:
            encoded_img = base64.b64encode(img_file.read()).decode()
        mascot_img_html = f'''
        <img src="data:image/png;base64,{encoded_img}" style="
            width: 95px;
            height: 95px;
            border-radius: 50%;
            border: 3px solid #00F2FE;
            box-shadow: 0 0 25px rgba(0, 242, 254, 0.6), 0 0 50px rgba(56, 189, 248, 0.3);
            object-fit: cover;
            animation: mascotFloat 3.5s ease-in-out infinite;
        ">
        '''

    # Interactive Speech Bubble Tips List
    tips = [
        "👋 <b>Hello! I'm ShieldBot — your AI Cyber Security Assistant!</b><br>I work 24/7 scanning videos for facial edge artifacts and AI voice cloning!",
        "💡 <b>Did you know?</b> Over 75% of deepfakes exhibit unnatural eye-blinking rates and mismatched skin lighting around the jawline!",
        "🩸 <b>Biological Pulse Test:</b> Real humans have continuous blood flow heartbeat pulses (rPPG). AI deepfake generators cannot copy human heartbeat waveforms!",
        "🚨 <b>Law Enforcement Clearance:</b> Police officers can use our <i>Cyber Cell</i> section to generate Court-Admissible Section 65B Digital Evidence Certificates!"
    ]

    # Session state for current tip index
    if "mascot_tip_idx" not in st.session_state:
        st.session_state["mascot_tip_idx"] = 0

    current_tip = tips[st.session_state["mascot_tip_idx"]]

    st.markdown(f"""
    <style>
    @keyframes mascotFloat {{
        0% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-10px) rotate(2deg); }}
        100% {{ transform: translateY(0px) rotate(0deg); }}
    }}
    @keyframes pulseGlow {{
        0% {{ box-shadow: 0 0 15px rgba(0, 242, 254, 0.4); }}
        50% {{ box-shadow: 0 0 35px rgba(0, 242, 254, 0.8); }}
        100% {{ box-shadow: 0 0 15px rgba(0, 242, 254, 0.4); }}
    }}
    </style>

    <div style="
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 100%);
        border: 2px solid rgba(0, 242, 254, 0.4);
        border-radius: 24px;
        padding: 24px 30px;
        margin-bottom: 28px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        position: relative;
    ">
        <div style="display: flex; align-items: center; gap: 24px; flex-wrap: wrap;">
            <div style="flex-shrink: 0; text-align: center;">
                {mascot_img_html}
                <div style="
                    margin-top: 8px;
                    background: rgba(0, 242, 254, 0.15);
                    color: #00F2FE;
                    border: 1px solid #00F2FE;
                    padding: 3px 12px;
                    border-radius: 12px;
                    font-size: 10px;
                    font-weight: 900;
                    letter-spacing: 1px;
                ">SHIELD BOT v1.0</div>
            </div>
            
            <div style="flex: 1; min-width: 260px;">
                <div style="
                    background: rgba(30, 41, 59, 0.85);
                    border: 1px solid rgba(56, 189, 248, 0.3);
                    border-radius: 18px;
                    padding: 18px 22px;
                    position: relative;
                    box-shadow: inset 0 1px 1px rgba(255,255,255,0.08);
                ">
                    <div style="font-size: 14px; color: #F8FAFC; line-height: 1.6; font-weight: 500;">
                        {current_tip}
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Mascot Tip Toggle Button
    col_b1, col_b2, col_b3 = st.columns([1, 1.5, 1])
    with col_b2:
        if st.button("💡 Ask ShieldBot For Another Tip!", use_container_width=True, key="btn_mascot_tip"):
            st.session_state["mascot_tip_idx"] = (st.session_state["mascot_tip_idx"] + 1) % len(tips)
            st.rerun()
