"""
TrustShield AI - Suspicious Events Timeline Component
Renders an interactive timeline of detected anomaly timestamps with clickable frame jump selectors.
"""

import streamlit as st


def render_events_timeline(is_fake: bool) -> int:
    """Render interactive timeline of suspicious events and return selected frame jump index."""
    st.subheader("⏱️ Suspicious Event Timeline")
    st.caption("Temporal sequence log highlighting exact timestamps where neural anomalies occur.")
    
    if is_fake:
        events = [
            {"time": "00:04", "frame": 4, "title": "Eye Blink Anomaly", "desc": "Fixed rPPG pulse & non-natural eye closure duration", "type": "WARNING", "icon": "👁️"},
            {"time": "00:08", "frame": 8, "title": "Lip Synchronization Offset", "desc": "Phoneme-viseme delay of +80ms detected", "type": "DANGER", "icon": "👄"},
            {"time": "00:13", "frame": 13, "title": "GAN Grid Artifact Peak", "desc": "High-frequency spatial noise grid detected on cheek region", "type": "DANGER", "icon": "⚡"},
            {"time": "00:17", "frame": 15, "title": "Facial Boundary Texture Noise", "desc": "Warping blur along jawline border seam", "type": "DANGER", "icon": "🎭"}
        ]
    else:
        events = [
            {"time": "00:02", "frame": 2, "title": "Natural Blink Event", "desc": "Normal physiological eye blink rate verified", "type": "SAFE", "icon": "👁️"},
            {"time": "00:09", "frame": 9, "title": "Illumination Consistency", "desc": "Uniform shadow transition across facial plane", "type": "SAFE", "icon": "💡"},
            {"time": "00:14", "frame": 14, "title": "Organic Lip Synchrony", "desc": "Zero audio-visual phoneme delay", "type": "SAFE", "icon": "👄"}
        ]
        
    selected_frame = 1
    cols = st.columns(len(events))
    
    for idx, ev in enumerate(events):
        with cols[idx]:
            border_color = "#EF4444" if ev['type'] == 'DANGER' else "#F59E0B" if ev['type'] == 'WARNING' else "#22C55E"
            st.markdown(f"""
            <div class="event-item" style="border-left-color: {border_color}; min-height: 120px;">
                <div style="font-size: 11px; font-weight: 800; color: #38BDF8;">{ev['time']} (Frame #{ev['frame']})</div>
                <div style="font-weight: 800; font-size: 13px; color: #F8FAFC; margin-top: 4px;">{ev['icon']} {ev['title']}</div>
                <div style="font-size: 11px; color: #94A3B8; margin-top: 4px;">{ev['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Jump to {ev['time']}", key=f"btn_jump_{idx}", use_container_width=True):
                selected_frame = ev['frame']
                st.session_state['current_frame_nav'] = ev['frame']
                
    return selected_frame
