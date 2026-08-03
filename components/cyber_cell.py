"""
TrustShield AI - Law Enforcement & Cyber Cell Portal Component
Renders the specialized Cyber Crime Cell evidence locker, Section 65B certificate overview, and restricted access coming soon status.
"""

import streamlit as st

POLICE = "🚓"
SHIELD = "🛡️"
LOCK   = "🔒"
FILE   = "📜"
WARN   = "⚠️"
CHECK  = "✅"
BADGE  = "🏷️"
SEARCH = "🔍"


def render_cyber_cell():
    """Render Law Enforcement & Cyber Crime Cell Unit section."""
    
    # 1. Official Police / Law Enforcement Header Banner
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 50%, rgba(30, 58, 138, 0.3) 100%);
        border: 2px solid #3B82F6;
        border-radius: 20px;
        padding: 28px 36px;
        margin-bottom: 24px;
        box-shadow: 0 15px 40px rgba(59, 130, 246, 0.25), inset 0 1px 1px rgba(255, 255, 255, 0.15);
    ">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;">
            <div style="display: flex; align-items: center; gap: 18px;">
                <div style="
                    font-size: 34px;
                    width: 60px;
                    height: 60px;
                    background: linear-gradient(135deg, rgba(59, 130, 246, 0.3), rgba(0, 242, 254, 0.3));
                    border: 2px solid #3B82F6;
                    border-radius: 16px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    box-shadow: 0 0 25px rgba(59, 130, 246, 0.4);
                ">{POLICE}</div>
                <div>
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                        <span style="background: rgba(59, 130, 246, 0.2); color: #60A5FA; border: 1px solid #3B82F6; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 900; letter-spacing: 1px;">
                            LAW ENFORCEMENT UNIT
                        </span>
                        <span style="background: rgba(245, 158, 11, 0.15); color: #F59E0B; border: 1px solid rgba(245, 158, 11, 0.4); padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 800; letter-spacing: 1px;">
                            RESTRICTED ACCESS PORTAL
                        </span>
                    </div>
                    <h1 style="font-size: 32px; font-weight: 900; background: linear-gradient(90deg, #60A5FA 0%, #38BDF8 50%, #00F2FE 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; letter-spacing: -0.5px;">
                        Law Enforcement & Cyber Crime Portal
                    </h1>
                    <p style="color: #CBD5E1; font-size: 15px; margin-top: 4px; font-weight: 600;">
                        Judicial Forensic Evidence Locker, FIR Audit Hashing & Court Admissibility Unit
                    </p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 2. Law Enforcement Portal Capabilities (Police Unit Features)
    st.subheader("🏛️ Specialized Law Enforcement Capabilities (Police & Cyber Cell Features)")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    
    with col_p1:
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.9); border: 2px solid rgba(59, 130, 246, 0.4); border-top: 5px solid #3B82F6; border-radius: 16px; padding: 22px; height: 100%;">
            <div style="font-size: 32px; margin-bottom: 8px;">📜</div>
            <h4 style="color: #60A5FA; font-size: 17px; font-weight: 900; margin-top: 0;">1. Section 65B Evidence Act Certification</h4>
            <p style="color: #CBD5E1; font-size: 13px; line-height: 1.7; font-weight: 500;">
                Generates Indian Evidence Act Sec 65B & Bharatiya Sakshya Adhiniyam (BSA) compliant digital certificates with cryptographic SHA-256 integrity seal for court presentation.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_p2:
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.9); border: 2px solid rgba(56, 189, 248, 0.4); border-top: 5px solid #38BDF8; border-radius: 16px; padding: 22px; height: 100%;">
            <div style="font-size: 32px; margin-bottom: 8px;">📁</div>
            <h4 style="color: #38BDF8; font-size: 17px; font-weight: 900; margin-top: 0;">2. FIR Case Number Evidence Locker</h4>
            <p style="color: #CBD5E1; font-size: 13px; line-height: 1.7; font-weight: 500;">
                Investigating Officers (I.O.) can tag scanned videos with FIR case numbers, Police Station IDs, and export tamper-evident forensic ZIP evidence packages.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_p3:
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.9); border: 2px solid rgba(168, 85, 247, 0.4); border-top: 5px solid #A855F7; border-radius: 16px; padding: 22px; height: 100%;">
            <div style="font-size: 32px; margin-bottom: 8px;">🕵️‍♂️</div>
            <h4 style="color: #A855F7; font-size: 17px; font-weight: 900; margin-top: 0;">3. Perpetrator Model Traceability</h4>
            <p style="color: #CBD5E1; font-size: 13px; line-height: 1.7; font-weight: 500;">
                Identifies synthetic generation pipeline artifacts (RoOP, DeepFaceLive, Sora, Face2Face) and extracts device EXIF metadata for cyber criminal tracing.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 32px;'></div>", unsafe_allow_html=True)

    # 3. Coming Soon Status Card (Restricted Unit Access)
    st.markdown(f"""
    <div style="
        background: rgba(15, 23, 42, 0.95);
        border: 2px solid rgba(59, 130, 246, 0.5);
        border-top: 6px solid #3B82F6;
        border-radius: 20px;
        padding: 36px 40px;
        text-align: center;
        margin-top: 10px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
    ">
        <div style="font-size: 46px; margin-bottom: 12px;">{LOCK}</div>
        <h3 style="color: #60A5FA; font-size: 24px; font-weight: 900; margin: 0;">
            RESTRICTED LAW ENFORCEMENT PORTAL — COMING SOON
        </h3>
        <p style="color: #CBD5E1; font-size: 14px; margin-top: 10px; font-weight: 500; max-width: 680px; margin-left: auto; margin-right: auto; line-height: 1.6;">
            This specialized Police & Cyber Crime Cell portal is currently undergoing official accreditation and security audit for official law enforcement agency authentication. Full portal integration will be unlocked in <b>TrustShield AI Enterprise v4.0</b>.
        </p>
        <div style="margin-top: 20px; display: flex; justify-content: center; gap: 12px; flex-wrap: wrap;">
            <span style="background: rgba(59, 130, 246, 0.2); color: #60A5FA; border: 1px solid #3B82F6; padding: 6px 18px; border-radius: 20px; font-size: 12px; font-weight: 900; letter-spacing: 1px;">
                STATUS: UNDER ACCREDITATION DEVELOPMENT
            </span>
            <span style="background: rgba(245, 158, 11, 0.15); color: #F59E0B; border: 1px solid #F59E0B; padding: 6px 18px; border-radius: 20px; font-size: 12px; font-weight: 900; letter-spacing: 1px;">
                SECURITY ACCESS: LEVEL 6 POLICE CLEARANCE REQUIRED
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
