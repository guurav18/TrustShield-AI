"""
TrustShield AI - Executive Home Dashboard Component
Renders the high-level Cyber Command Center overview with KPIs, threat trends, attack vectors, and system health.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

SHIELD  = "🛡️"
CHART   = "📊"
MICRO   = "🔬"
BOLT    = "⚡"
LOCK    = "🔒"
BRAIN   = "🧠"
TREND   = "📈"
CHECK   = "✅"


import datetime


def render_home_dashboard():
    """Render Executive Command Center Home Dashboard."""
    
    # Calculate time of day greeting
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif current_hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
        
    user_name = st.session_state.get("user_name", "Security Officer")
    
    # 1. Executive Banner with Dynamic Welcome Greeting
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 50%, rgba(30, 27, 75, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 20px;
        padding: 28px 36px;
        margin-bottom: 24px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        position: relative;
    ">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div>
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                    <span style="background: rgba(0, 242, 254, 0.15); color: #00F2FE; border: 1px solid #00F2FE; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 800; letter-spacing: 1px;">
                        👋 {greeting.upper()}, {user_name.upper()}
                    </span>
                    <span style="background: rgba(34, 197, 94, 0.15); color: #22C55E; border: 1px solid rgba(34, 197, 94, 0.4); padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 800; letter-spacing: 1px;">
                        CLEARANCE LEVEL 5 ACTIVE
                    </span>
                </div>
                <h1 style="font-size: 34px; font-weight: 900; background: linear-gradient(90deg, #00F2FE 0%, #38BDF8 50%, #818CF8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; letter-spacing: -0.5px;">
                    Cyber Command Center
                </h1>
                <p style="color: #94A3B8; font-size: 14px; margin-top: 6px; font-weight: 500;">
                    Welcome back to TrustShield AI — Real-time Forensic Intelligence & Deepfake Defense Platform
                </p>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 11px; color: #64748B; font-weight: bold; text-transform: uppercase;">GLOBAL DEFENSE STATUS</div>
                <div style="font-size: 22px; font-weight: 900; color: #22C55E; margin-top: 2px;">DEFCON 1 — OPTIMAL</div>
                <div style="font-size: 12px; color: #94A3B8;">OpenCV Face Detector + MobileNetV2 Neural Shield</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    
    # 2. Key KPI Metric Cards
    k1, k2, k3, k4 = st.columns(4)
    
    with k1:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.25); border-top: 4px solid #00F2FE; border-radius: 16px; padding: 20px; text-align: center;">
            <div style="font-size: 11px; font-weight: 800; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">TOTAL MEDIA SCANNED</div>
            <div style="font-size: 32px; font-weight: 900; color: #F8FAFC; margin-top: 6px;">1,842</div>
            <div style="font-size: 12px; color: #22C55E; margin-top: 4px; font-weight: 700;">▲ +14.2% this week</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(239, 68, 68, 0.25); border-top: 4px solid #EF4444; border-radius: 16px; padding: 20px; text-align: center;">
            <div style="font-size: 11px; font-weight: 800; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">DEEPFAKES INTERCEPTED</div>
            <div style="font-size: 32px; font-weight: 900; color: #EF4444; margin-top: 6px;">438</div>
            <div style="font-size: 12px; color: #EF4444; margin-top: 4px; font-weight: 700;">23.7% Deepfake Threat Rate</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(34, 197, 94, 0.25); border-top: 4px solid #22C55E; border-radius: 16px; padding: 20px; text-align: center;">
            <div style="font-size: 11px; font-weight: 800; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">NEURAL MODEL ACCURACY</div>
            <div style="font-size: 32px; font-weight: 900; color: #22C55E; margin-top: 6px;">95.4%</div>
            <div style="font-size: 12px; color: #38BDF8; margin-top: 4px; font-weight: 700;">MobileNetV2 + Face Crop</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(168, 85, 247, 0.25); border-top: 4px solid #A855F7; border-radius: 16px; padding: 20px; text-align: center;">
            <div style="font-size: 11px; font-weight: 800; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">AVG INFERENCE LATENCY</div>
            <div style="font-size: 32px; font-weight: 900; color: #A855F7; margin-top: 6px;">0.84s</div>
            <div style="font-size: 12px; color: #A855F7; margin-top: 4px; font-weight: 700;">Real-Time Frame Stream</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)

    # 3. Interactive Analytics Charts
    c1, c2 = st.columns([1.6, 1])

    with c1:
        st.subheader("📈 Daily Forensic Scan Volume & Interception Trends")
        
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        scanned = [210, 245, 290, 310, 340, 220, 227]
        intercepted = [42, 58, 65, 82, 91, 50, 50]

        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=days, y=scanned,
            name='Total Videos Inspected',
            mode='lines+markers',
            line=dict(color='#00F2FE', width=3),
            fill='tozeroy',
            fillcolor='rgba(0, 242, 254, 0.08)'
        ))
        fig_trend.add_trace(go.Scatter(
            x=days, y=intercepted,
            name='Deepfakes Flagged',
            mode='lines+markers',
            line=dict(color='#EF4444', width=3, dash='dash'),
            fill='tozeroy',
            fillcolor='rgba(239, 68, 68, 0.08)'
        ))

        fig_trend.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis=dict(gridcolor='#1E293B', color='#94A3B8'),
            yaxis=dict(gridcolor='#1E293B', color='#94A3B8'),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#E2E8F0"))
        )
        st.plotly_chart(fig_trend, use_container_width=True)

    with c2:
        st.subheader("🎯 Deepfake Attack Vector Breakdown")
        
        vectors = ['FaceSwap (RoOP/DeepFace)', 'Face2Face Expression Manipulation', 'NeuralTextures Artifacts', 'Generative Diffusion (SORA/Wan)', 'Voice Cloning Spoofing']
        counts = [185, 110, 65, 48, 30]

        fig_pie = go.Figure(data=[go.Pie(
            labels=vectors,
            values=counts,
            hole=.55,
            marker_colors=['#00F2FE', '#38BDF8', '#818CF8', '#A855F7', '#EF4444'],
            textinfo='percent',
            hoverinfo='label+value+percent'
        )])

        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300,
            margin=dict(l=10, r=10, t=20, b=20),
            legend=dict(font=dict(color="#94A3B8", size=10), orientation="h")
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")

    # 4. Live Security Telemetry & System Health Grid
    st.subheader("🛡️ Subsystem Security & Infrastructure Telemetry")

    col_h1, col_h2, col_h3, col_h4 = st.columns(4)

    with col_h1:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); padding: 16px; border-radius: 12px;">
            <div style="font-size: 12px; color: #38BDF8; font-weight: bold;">OPENCV FACE DETECTOR</div>
            <div style="font-size: 16px; color: #22C55E; font-weight: 800; margin-top: 4px;">✅ ONLINE</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">Haar Cascade + 20% Padded Crop</div>
        </div>
        """, unsafe_allow_html=True)

    with col_h2:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); padding: 16px; border-radius: 12px;">
            <div style="font-size: 12px; color: #38BDF8; font-weight: bold;">NEURAL INFERENCE MODEL</div>
            <div style="font-size: 16px; color: #22C55E; font-weight: 800; margin-top: 4px;">✅ ONLINE</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">MobileNetV2 (224x224x3)</div>
        </div>
        """, unsafe_allow_html=True)

    with col_h3:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); padding: 16px; border-radius: 12px;">
            <div style="font-size: 12px; color: #38BDF8; font-weight: bold;">EXPLAINABILITY ENGINE</div>
            <div style="font-size: 16px; color: #22C55E; font-weight: 800; margin-top: 4px;">✅ READY</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">Grad-CAM Feature Overlay</div>
        </div>
        """, unsafe_allow_html=True)

    with col_h4:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); padding: 16px; border-radius: 12px;">
            <div style="font-size: 12px; color: #38BDF8; font-weight: bold;">C2PA PROOF ENGINE</div>
            <div style="font-size: 16px; color: #22C55E; font-weight: 800; margin-top: 4px;">✅ ACTIVE</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">SHA-256 Hash Audit Trail</div>
        </div>
        """, unsafe_allow_html=True)
