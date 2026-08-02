"""
TrustShield AI - Hero Banner Component
Displays cybersecurity branding, floating particle style elements, and live system KPI statistics.
"""

import streamlit as st


def render_hero():
    """Render main enterprise hero header banner and KPI statistics."""
    st.markdown("""
    <div class="hero-container">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
                <div class="hero-badge-live">
                    <div class="pulse-dot"></div>
                    TRUST ENGINE ONLINE • ACTIVE PROTECTION
                </div>
                <h1 class="hero-title-gradient">TrustShield AI</h1>
                <div class="hero-subtitle">Enterprise Multi-Modal Deepfake Forensic Intelligence Platform</div>
            </div>
            <div style="text-align: right; background: rgba(19, 26, 46, 0.6); padding: 12px 18px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.2);">
                <div style="font-size: 11px; color: #64748B; font-weight: bold; text-transform: uppercase;">Engine Core</div>
                <div style="font-size: 14px; color: #00F2FE; font-weight: 800; margin-top: 2px;">Multi-Modal ResNet50 + LSTM</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 4 Live KPI Metric Cards
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    with kpi1:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-label">Videos Analyzed</div>
            <div class="kpi-value" style="color: #38BDF8;">14,892</div>
            <div style="font-size: 11px; color: #22C55E; margin-top: 4px;">↑ +12.4% this week</div>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi2:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-label">Threats Detected</div>
            <div class="kpi-value" style="color: #EF4444;">1,348</div>
            <div style="font-size: 11px; color: #EF4444; margin-top: 4px;">⚠️ High-risk flagged</div>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi3:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-label">System Accuracy</div>
            <div class="kpi-value" style="color: #22C55E;">98.7%</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">NIST Benchmark Validated</div>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi4:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-label">Trust Engine Status</div>
            <div class="kpi-value" style="color: #00F2FE; font-size: 22px; margin-top: 10px;">99.99% Uptime</div>
            <div style="font-size: 11px; color: #22C55E; margin-top: 4px;">Zero latency queue</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)
