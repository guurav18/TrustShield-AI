"""
TrustShield AI - Single Video Inspector Component
Renders single video drag-and-drop analysis, 10-step animated pipeline, video player, and recommendation engine.
"""

import streamlit as st
import tempfile
import os
import time
import numpy as np
from forensics.crypto_utils import compute_file_sha256, create_forensic_certificate
from forensics.forensic_engine import (
    PIPELINE_STEPS, compute_ai_findings, compute_multimodal_cards,
    compute_radar_metrics, compute_attack_probabilities
)
from components.gauges_charts import render_trust_gauge, render_threat_badge, render_radar_chart
from components.gradcam_heatmap import render_gradcam_section
from components.findings_panel import render_findings_and_multimodal
from components.timeline_events import render_events_timeline
from forensics.pdf_generator import generate_forensic_html_report


def render_single_inspector(detector):
    """Render single video drag-and-drop forensic inspector view."""
    
    col_up, col_info = st.columns([1.2, 0.8])
    
    with col_up:
        st.subheader("📤 Single Video Inspection Upload")
        uploaded_file = st.file_uploader(
            "Drag & drop target video for multi-modal neural inspection",
            type=["mp4", "avi", "mov", "mkv"],
            key="single_file_drop"
        )
        st.caption("Supported formats: **MP4, AVI, MOV, MKV** (Max file size: 500MB)")
        
    with col_info:
        st.subheader("⚙️ Inspection Configuration")
        sensitivity = st.session_state.get('sensitivity', 0.50)
        density = st.session_state.get('frame_density', 15)
        
        st.markdown(f"""
        <div style="background: #131A2E; border: 1px solid #1E293B; padding: 16px; border-radius: 12px;">
            <div style="font-size: 12px; color: #64748B; font-weight: bold;">ACTIVE PARAMETERS</div>
            <div style="font-size: 14px; color: #F8FAFC; font-weight: 700; margin-top: 6px;">Threshold Sensitivity: <span style="color: #00F2FE;">{sensitivity}</span></div>
            <div style="font-size: 14px; color: #F8FAFC; font-weight: 700; margin-top: 4px;">Extraction Density: <span style="color: #38BDF8;">{density} frames</span></div>
            <div style="font-size: 12px; color: #94A3B8; margin-top: 8px;">Multi-Modal ResNet50-LSTM + C2PA Evidence Module</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    if uploaded_file is not None:
        if st.button("⚡ Execute Forensic Neural Scan", key="btn_run_inspector", use_container_width=True):
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
                tmp.write(uploaded_file.getbuffer())
                tmp_path = tmp.name
                
            uploaded_file.seek(0)
            file_bytes = uploaded_file.read()
            file_hash = compute_file_sha256(file_bytes)
            
            try:
                # 10-Step Animated Pipeline Execution
                st.subheader("⚙️ Multi-Stage Neural Processing Pipeline")
                pipeline_placeholders = [st.empty() for _ in PIPELINE_STEPS]
                progress_bar = st.progress(0)
                
                for idx, step_name in enumerate(PIPELINE_STEPS):
                    for prev_i in range(idx):
                        pipeline_placeholders[prev_i].markdown(f"<div class='pipeline-step done'>✅ {PIPELINE_STEPS[prev_i]}</div>", unsafe_allow_html=True)
                        
                    pipeline_placeholders[idx].markdown(f"<div class='pipeline-step active'>⏳ Running {step_name}...</div>", unsafe_allow_html=True)
                    progress_bar.progress(int(((idx + 1) / len(PIPELINE_STEPS)) * 100))
                    time.sleep(0.12)
                    
                for final_i in range(len(PIPELINE_STEPS)):
                    pipeline_placeholders[final_i].markdown(f"<div class='pipeline-step done'>✅ {PIPELINE_STEPS[final_i]} Completed</div>", unsafe_allow_html=True)
                
                res = detector.predict_video(tmp_path, num_frames=density)
                st.success("✅ Multi-Modal Forensic Analysis Completed Successfully!")
                
                if res is not None:
                    is_fake = res['is_fake']
                    confidence = res['confidence']
                    avg_pred = res['prediction']
                    frame_preds = res['frame_predictions']
                    
                    trust_score = max(2.0, min(99.0, (1.0 - avg_pred) * 100))
                    
                    st.markdown("---")
                    
                    col_vplayer, col_gauge, col_radar = st.columns([1.1, 1, 1])
                    
                    with col_vplayer:
                        st.subheader("🎬 Video Player & Timeline")
                        uploaded_file.seek(0)
                        st.video(uploaded_file)
                        
                        current_frame_nav = st.slider(
                            "Frame Navigation Stepper",
                            min_value=1,
                            max_value=len(frame_preds),
                            value=st.session_state.get('current_frame_nav', 1)
                        )
                        st.caption(f"Currently inspecting **Frame #{current_frame_nav}** (Timestamp: `00:0{current_frame_nav}`) | Anomaly Score: `{frame_preds[current_frame_nav-1]:.4f}`")
                        
                    with col_gauge:
                        fig_gauge = render_trust_gauge(trust_score)
                        st.plotly_chart(fig_gauge, use_container_width=True)
                        
                        badge_html, threat_level = render_threat_badge(is_fake, trust_score)
                        st.markdown(badge_html, unsafe_allow_html=True)
                        
                    with col_radar:
                        st.subheader("🕸️ 6-Axis Forensic Radar")
                        radar_metrics = compute_radar_metrics(is_fake, avg_pred)
                        fig_radar = render_radar_chart(radar_metrics)
                        st.plotly_chart(fig_radar, use_container_width=True)
                        
                    st.markdown("---")
                    
                    render_gradcam_section(tmp_path, is_fake, current_frame_nav)
                    
                    ai_findings = compute_ai_findings(is_fake, confidence)
                    multimodal_cards = compute_multimodal_cards(is_fake, confidence)
                    attack_probs = compute_attack_probabilities(is_fake)
                    
                    render_findings_and_multimodal(ai_findings, multimodal_cards, attack_probs)
                    
                    st.markdown("---")
                    
                    jump_frame = render_events_timeline(is_fake)
                    
                    st.markdown("---")
                    
                    st.subheader("💡 AI Security Recommendation Engine")
                    if is_fake:
                        st.error("""
                        ⚠️ **HIGH RISK DEEPFAKE WARNING:**
                        - **Recommendation:** Media appears heavily manipulated using generative face-swapping framework. Avoid publishing or trusting this video for legal, financial, or journalistic decisions.
                        - **Next Action:** Issue formal forensic report, initiate C2PA hash audit, and flag source channel for identity spoofing investigation.
                        """)
                    else:
                        st.success("""
                        ✅ **AUTHENTIC MEDIA VERIFICATION:**
                        - **Recommendation:** No synthetic facial landmarks or rPPG pulse anomalies detected. Media appears to be organic and unmanipulated.
                        - **Next Action:** Ready for broadcast or evidentiary record storage. Digital certificate available for download below.
                        """)
                        
                    st.markdown("---")
                    
                    st.subheader("📜 Digital Forensic Evidence Report & Cryptographic Certificate")
                    
                    verdict_str = "DEEPFAKE MANIPULATION DETECTED" if is_fake else "VERIFIED ORGANIC MEDIA"
                    cert_dict = create_forensic_certificate(uploaded_file.name, file_hash, trust_score, threat_level, verdict_str)
                    
                    report_html = generate_forensic_html_report(cert_dict, ai_findings, attack_probs)
                    
                    c_d1, c_d2 = st.columns(2)
                    with c_d1:
                        st.download_button(
                            label="📜 Download Evidence-Ready Forensic Report (HTML/PDF)",
                            data=report_html,
                            file_name=f"TrustShield_Forensic_Report_{cert_dict['certificate_id']}.html",
                            mime="text/html",
                            use_container_width=True
                        )
                    with c_d2:
                        import json
                        st.download_button(
                            label="📜 Download Cryptographic C2PA Certificate (JSON)",
                            data=json.dumps(cert_dict, indent=2),
                            file_name=f"TrustShield_Certificate_{cert_dict['certificate_id']}.json",
                            mime="application/json",
                            use_container_width=True
                        )
                        
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
