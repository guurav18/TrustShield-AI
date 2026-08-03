"""
TrustShield AI - AI Findings & Multi-Modal Panel Component
Renders multi-modal status cards, AI findings breakdown, and attack classification probabilities.
"""

import streamlit as st
import plotly.express as px
import pandas as pd


def render_findings_and_multimodal(ai_findings: list, multimodal_cards: list, attack_probs: dict):
    """Render AI findings panel, multi-modal cards, and attack vector probabilities."""
    
    st.markdown("---")
    col_find, col_multi = st.columns([1.1, 0.9])
    
    with col_find:
        st.subheader("🔬 AI Forensic Findings Panel")
        st.caption("Granular neural vector anomaly breakdown across spatial and temporal dimensions.")
        
        for f in ai_findings:
            color = "#EF4444" if f['status'] in ['CRITICAL', 'HIGH'] else "#22C55E"
            st.markdown(f"""
            <div class="modal-card">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="font-size: 22px;">{f['icon']}</div>
                    <div>
                        <div style="font-weight: 700; font-size: 14px; color: #F8FAFC;">{f['finding']}</div>
                        <div style="font-size: 11px; color: #64748B;">Neural Anomaly Vector</div>
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-weight: 900; font-size: 15px; color: {color};">{f['confidence']:.1f}%</div>
                    <div style="font-size: 10px; font-weight: bold; color: {color}; text-transform: uppercase;">{f['status']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    with col_multi:
        st.subheader("📊 Multi-Modal Sensor Status")
        st.caption("State monitoring across 6 independent verification engines.")
        
        for card in multimodal_cards:
            st.markdown(f"""
            <div style="background: #131A2E; border: 1px solid #1E293B; border-left: 4px solid {card['color']}; padding: 12px 16px; border-radius: 10px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 18px;">{card['icon']}</span>
                    <div>
                        <div style="font-size: 13px; font-weight: 700; color: #F8FAFC;">{card['title']}</div>
                        <div style="font-size: 11px; color: {card['color']}; font-weight: 600;">{card['status']}</div>
                    </div>
                </div>
                <div style="font-size: 14px; font-weight: 800; color: #F8FAFC;">{card['confidence']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Attack Classification Probabilities
    st.subheader("⚡ Attack Vector Classification")
    st.caption("Machine learning identification of the generative framework used to synthesize media.")
    
    col_at1, col_at2 = st.columns([1.2, 0.8])
    
    with col_at1:
        df_at = pd.DataFrame({
            "Attack Vector": list(attack_probs.keys()),
            "Probability (%)": list(attack_probs.values())
        })
        
        fig_at = px.bar(
            df_at,
            x="Probability (%)",
            y="Attack Vector",
            orientation='h',
            color="Probability (%)",
            color_continuous_scale=["#38BDF8", "#818CF8", "#EF4444"],
            text="Probability (%)"
        )
        
        fig_at.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#94A3B8"),
            height=220,
            margin=dict(l=10, r=10, t=10, b=10),
            coloraxis_showscale=False
        )
        fig_at.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig_at, use_container_width=True)
        
    with col_at2:
        top_attack = max(attack_probs, key=attack_probs.get)
        top_prob = attack_probs[top_attack]
        
        st.markdown(f"""
        <div style="background: #131A2E; border: 1px solid rgba(129, 140, 248, 0.3); padding: 20px; border-radius: 12px; height: 100%;">
            <div style="font-size: 11px; color: #818CF8; font-weight: bold; text-transform: uppercase;">PRIMARY ATTACK TYPE IDENTIFIED</div>
            <div style="font-size: 22px; font-weight: 900; color: #F8FAFC; margin-top: 6px;">{top_attack}</div>
            <div style="font-size: 14px; color: #38BDF8; font-weight: 800; margin-top: 2px;">{top_prob:.1f}% Confidence Match</div>
            <div style="font-size: 12px; color: #94A3B8; margin-top: 10px;">
                Identified based on facial auto-encoder latent space compression boundaries and inter-ocular distance warping patterns.
            </div>
        </div>
        """, unsafe_allow_html=True)
