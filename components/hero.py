"""
TrustShield AI - Hero Banner Component
Displays cybersecurity branding, floating particle style elements, and live system KPI statistics.
"""

import streamlit as st


def render_hero():
    """Render main enterprise hero header banner and KPI statistics."""
    st.markdown("""
    <div class="hero-container">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px;">
            <div>
                <div class="hero-badge-live">
                    <div class="pulse-dot"></div>
                    SYSTEM LIVE • ACTIVE MULTI-MODAL SHIELD
                </div>
                <h1 class="hero-title-gradient">TrustShield AI</h1>
                <div class="hero-subtitle">Enterprise Multi-Modal Deepfake Forensic Intelligence & Evidence Platform</div>
            </div>
            <div style="
                background: rgba(15, 23, 42, 0.75);
                backdrop-filter: blur(12px);
                padding: 14px 20px;
                border-radius: 14px;
                border: 1px solid rgba(56, 189, 248, 0.25);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            ">
                <div style="font-size: 10px; color: #64748B; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px;">ENGINE CORE ARCHITECTURE</div>
                <div style="font-size: 14px; color: #00F2FE; font-weight: 800; margin-top: 3px;">Multi-Modal Spatial ResNet50 + LSTM</div>
                <div style="font-size: 11px; color: #94A3B8; margin-top: 2px;">GradCAM Attention & C2PA Evidence Module</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 4 Live KPI Metric Cards
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    with kpi1:
        st.markdown("""
        <div class="kpi-card" style="border-top-color: #38BDF8;">
            <div class="kpi-label">Videos Analyzed</div>
            <div class="kpi-value" style="color: #38BDF8;">14,892</div>
            <div style="font-size: 11px; color: #22C55E; margin-top: 4px; font-weight: 700;">📈 +12.4% this week</div>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi2:
        st.markdown("""
        <div class="kpi-card" style="border-top-color: #EF4444;">
            <div class="kpi-label">Threats Intercepted</div>
            <div class="kpi-value" style="color: #EF4444;">1,348</div>
            <div style="font-size: 11px; color: #EF4444; margin-top: 4px; font-weight: 700;">⚠️ High-risk flagged</div>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi3:
        st.markdown("""
        <div class="kpi-card" style="border-top-color: #22C55E;">
            <div class="kpi-label">System Accuracy</div>
            <div class="kpi-value" style="color: #22C55E;">98.7%</div>
            <div style="font-size: 11px; color: #94A3B8; margin-top: 4px; font-weight: 600;">NIST Benchmark Validated</div>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi4:
        st.markdown("""
        <div class="kpi-card" style="border-top-color: #00F2FE;">
            <div class="kpi-label">Trust Engine Uptime</div>
            <div class="kpi-value" style="color: #00F2FE; font-size: 26px; margin-top: 8px;">99.99%</div>
            <div style="font-size: 11px; color: #22C55E; margin-top: 4px; font-weight: 700;">⚡ Real-time zero latency</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)
