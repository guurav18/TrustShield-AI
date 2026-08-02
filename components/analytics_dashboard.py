"""
TrustShield AI - Analytics Dashboard Component
Renders enterprise operational metrics, attack distribution bar charts, line charts, and pie charts.
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np


def render_analytics_dashboard():
    """Render enterprise security analytics and trend charts."""
    st.subheader("📈 Operational Analytics & Threat Metrics")
    st.caption("Real-time telemetry and trend insights across global media verification nodes.")
    
    # KPI Row
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Scanned Media", "14,892", delta="+12.4% vs last week")
    k2.metric("Authentic Media Ratio", "90.95%", delta="13,544 verified")
    k3.metric("Deepfakes Intercepted", "1,348", delta="+3.1% threat surge", delta_color="inverse")
    k4.metric("Avg Detection Speed", "1.42s / video", delta="-0.15s optimal")
    
    st.markdown("---")
    
    col_chart1, col_chart2 = st.columns([1, 1])
    
    with col_chart1:
        st.subheader("📊 Media Classification Distribution")
        df_pie = pd.DataFrame({
            "Classification": ["Authentic Media", "Deepfake FaceSwap", "Generative AI (Sora/Runway)", "Lip-Sync Manipulated"],
            "Count": [13544, 782, 364, 202]
        })
        fig_pie = px.pie(
            df_pie,
            names="Classification",
            values="Count",
            color="Classification",
            color_discrete_map={
                "Authentic Media": "#22C55E",
                "Deepfake FaceSwap": "#EF4444",
                "Generative AI (Sora/Runway)": "#F97316",
                "Lip-Sync Manipulated": "#F59E0B"
            },
            hole=0.45
        )
        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#94A3B8"),
            height=320,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_chart2:
        st.subheader("📈 Daily Threat Ingress (30 Days)")
        dates = pd.date_range(end=pd.Timestamp.now(), periods=30, freq='D')
        daily_fakes = np.random.randint(25, 65, size=30) + np.sin(np.linspace(0, 5, 30)) * 15
        
        df_line = pd.DataFrame({"Date": dates, "Flagged Deepfakes": daily_fakes})
        fig_line = px.line(
            df_line,
            x="Date",
            y="Flagged Deepfakes",
            line_shape="spline",
            color_discrete_sequence=["#00F2FE"]
        )
        fig_line.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#94A3B8"),
            xaxis=dict(gridcolor="#1E293B"),
            yaxis=dict(gridcolor="#1E293B"),
            height=320,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig_line, use_container_width=True)
        
    st.markdown("---")
    
    st.subheader("🎭 Attack Framework Distribution Breakdown")
    df_bar = pd.DataFrame({
        "Generative Framework": ["DeepFaceLab", "FaceSwap", "FaceFusion", "HeyGen / ElevenLabs", "Runway Gen-2", "OpenAI Sora", "SadTalker"],
        "Detected Attacks": [542, 380, 210, 145, 98, 45, 30]
    })
    
    fig_bar = px.bar(
        df_bar,
        x="Generative Framework",
        y="Detected Attacks",
        color="Detected Attacks",
        color_continuous_scale=["#38BDF8", "#818CF8", "#EF4444"]
    )
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#94A3B8"),
        xaxis=dict(gridcolor="#1E293B"),
        yaxis=dict(gridcolor="#1E293B"),
        height=300,
        margin=dict(l=20, r=20, t=20, b=20),
        coloraxis_showscale=False
    )
    st.plotly_chart(fig_bar, use_container_width=True)
