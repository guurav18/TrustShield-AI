"""
TrustShield AI - Gauges & Radar Charts Component
Renders Plotly circular trust score gauge, threat level indicators, and 6-axis radar charts.
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np


def render_trust_gauge(trust_score: float) -> go.Figure:
    """Create a high-tech Plotly circular gauge for Trust Score (0-100)."""
    # Color logic
    if trust_score >= 80:
        bar_color = "#22C55E"
    elif trust_score >= 60:
        bar_color = "#EAB308"
    elif trust_score >= 40:
        bar_color = "#F59E0B"
    elif trust_score >= 20:
        bar_color = "#F97316"
    else:
        bar_color = "#EF4444"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=trust_score,
        number={'suffix': " / 100", 'font': {'size': 38, 'color': "#F8FAFC", 'family': "Inter"}},
        title={'text': "TRUST SCORE ENGINE", 'font': {'size': 14, 'color': "#94A3B8", 'family': "Inter"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#334155"},
            'bar': {'color': bar_color, 'thickness': 0.3},
            'bgcolor': "#0B1020",
            'bordercolor': "rgba(255,255,255,0.05)",
            'steps': [
                {'range': [0, 30], 'color': "rgba(239, 68, 68, 0.15)"},
                {'range': [30, 70], 'color': "rgba(245, 158, 11, 0.15)"},
                {'range': [70, 100], 'color': "rgba(34, 197, 94, 0.15)"}
            ]
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=260,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig


def render_threat_badge(is_fake: bool, trust_score: float) -> tuple:
    """Calculate threat level and return badge HTML."""
    if not is_fake and trust_score >= 80:
        level = "SAFE"
        color = "#22C55E"
        rating = "Very High Authenticity"
        bg = "rgba(34, 197, 94, 0.15)"
        border = "#22C55E"
    elif not is_fake and trust_score >= 50:
        level = "SUSPICIOUS"
        color = "#F59E0B"
        rating = "Medium Authenticity"
        bg = "rgba(245, 158, 11, 0.15)"
        border = "#F59E0B"
    elif is_fake and trust_score >= 25:
        level = "HIGH RISK"
        color = "#F97316"
        rating = "Low Authenticity"
        bg = "rgba(249, 115, 22, 0.15)"
        border = "#F97316"
    else:
        level = "CRITICAL"
        color = "#EF4444"
        rating = "Critical Deepfake Risk"
        bg = "rgba(239, 68, 68, 0.2)"
        border = "#EF4444"

    badge_html = f"""<div style="background: {bg}; border: 1px solid {border}; padding: 16px; border-radius: 12px; text-align: center; margin-top: 10px;">
<div style="font-size: 11px; color: #94A3B8; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">THREAT LEVEL</div>
<div style="font-size: 26px; font-weight: 900; color: {color}; margin-top: 4px;">{level}</div>
<div style="font-size: 12px; color: #E2E8F0; margin-top: 2px;">Authenticity Rating: <b>{rating}</b></div>
</div>"""
    return badge_html, level


def render_radar_chart(radar_data: dict) -> go.Figure:
    """Create a 6-axis Plotly Forensic Radar chart."""
    categories = list(radar_data.keys())
    values = list(radar_data.values())
    
    # Close polygon
    categories_plot = categories + [categories[0]]
    values_plot = values + [values[0]]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values_plot,
        theta=categories_plot,
        fill='toself',
        fillcolor='rgba(0, 242, 254, 0.15)',
        line=dict(color='#00F2FE', width=2),
        name='Forensic Vectors'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1.0 if max(values) <= 1.0 else 100],
                color='#64748B',
                gridcolor='#1E293B'
            ),
            angularaxis=dict(
                color='#94A3B8',
                gridcolor='#1E293B'
            ),
            bgcolor='#0B1020'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=320,
        margin=dict(l=40, r=40, t=30, b=30),
        showlegend=False
    )
    return fig
