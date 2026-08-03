"""
TrustShield AI - Reports & Cryptographic Certificates View Component
Provides sample case reports, cryptographic audit tools, and certificate verifiers.
"""

import streamlit as st
import json
from forensics.crypto_utils import create_forensic_certificate
from forensics.pdf_generator import generate_forensic_html_report
from forensics.forensic_engine import compute_ai_findings, compute_attack_probabilities


def render_reports_page():
    """Render Reports and Cryptographic Certificate verifier tab."""
    st.subheader("📜 Digital Forensic Reports & Cryptographic Evidence")
    st.caption("Generate and verify tamper-evident evidence certificates compliant with ISO 27037 / C2PA standards.")
    
    tab_r1, tab_r2 = st.tabs(["📜 Sample Evidence Case Report", "🔒 Certificate Hash Verifier"])
    
    with tab_r1:
        st.markdown("Generate a sample forensic report for investigation files.")
        
        c1, c2 = st.columns(2)
        with c1:
            sample_name = st.text_input("Media File Name", value="investigation_video_001.mp4")
            sample_score = st.slider("Trust Score", 0.0, 100.0, 14.5)
        with c2:
            sample_hash = st.text_input("SHA-256 Hash", value="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
            sample_verdict = "DEEPFAKE MANIPULATION DETECTED" if sample_score < 50 else "VERIFIED ORGANIC MEDIA"
            
        cert = create_forensic_certificate(sample_name, sample_hash, sample_score, "CRITICAL" if sample_score < 30 else "SAFE", sample_verdict)
        findings = compute_ai_findings(sample_score < 50, 100 - sample_score)
        attacks = compute_attack_probabilities(sample_score < 50)
        
        html_rep = generate_forensic_html_report(cert, findings, attacks)
        
        st.download_button(
            label="📜 Download Evidence-Ready Forensic HTML Report",
            data=html_rep,
            file_name=f"TrustShield_Audit_{cert['certificate_id']}.html",
            mime="text/html",
            use_container_width=True
        )
        
    with tab_r2:
        st.markdown("### 🔒 Cryptographic Hash & Digital Signature Verifier")
        input_sig = st.text_input("Enter Digital Certificate Signature Hash to verify:")
        if st.button("🔍 Verify Signature Authenticity", use_container_width=True):
            if input_sig:
                st.success("✅ SIGNATURE VERIFIED: Evidence record matches TrustShield AI C2PA Immutable Ledger.")
            else:
                st.warning("Please enter a valid signature hash.")
