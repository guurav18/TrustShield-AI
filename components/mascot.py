"""
TrustShield AI - ShieldBot Animated Toast Assistant Component
Renders a floating bottom-right 3D Cyber Bot toast popup that automatically disappears after 18 seconds.
"""

import streamlit as st


def render_mascot_widget():
    """Render floating animated ShieldBot toast popup that automatically disappears after 18s."""
    
    st.markdown("""
    <style>
    @keyframes slideInRight {
        0% { transform: translateX(120%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    @keyframes mascotBounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }
    </style>

    <div id="mascot-toast" style="
        position: fixed;
        bottom: 24px;
        right: 24px;
        z-index: 999999;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.96) 0%, rgba(30, 41, 59, 0.95) 100%);
        border: 2px solid #00F2FE;
        border-radius: 20px;
        padding: 16px 20px;
        box-shadow: 0 12px 40px rgba(0, 242, 254, 0.35), 0 0 20px rgba(0, 0, 0, 0.8);
        display: flex;
        align-items: center;
        gap: 16px;
        max-width: 380px;
        animation: slideInRight 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        backdrop-filter: blur(12px);
    ">
        <div style="
            font-size: 38px;
            width: 58px;
            height: 58px;
            background: linear-gradient(135deg, rgba(0, 242, 254, 0.25), rgba(56, 189, 248, 0.2));
            border: 1.5px solid #00F2FE;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            animation: mascotBounce 2.5s ease-in-out infinite;
        ">🤖</div>
        <div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 11px; font-weight: 900; color: #00F2FE; letter-spacing: 1px;">SHIELD</span>
                <span style="background: rgba(34, 197, 94, 0.2); color: #22C55E; border: 1px solid #22C55E; padding: 2px 8px; border-radius: 10px; font-size: 9px; font-weight: 900;">ONLINE</span>
            </div>
            <div style="font-size: 13px; color: #F8FAFC; margin-top: 5px; font-weight: 500; line-height: 1.45;">
                👋 <b>Hello! I'm TrustShield!</b><br>
                Welcome! I'm scanning all media for AI deepfakes and face swaps in real-time. Stay safe!
            </div>
        </div>
    </div>


    <script>
    setTimeout(function() {
        var toast = document.getElementById('mascot-toast');
        if (toast) {
            toast.style.transition = 'opacity 1s ease-out, transform 1s ease-out';
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(25px)';
            setTimeout(function() { toast.remove(); }, 1000);
        }
    }, 18000);
    </script>
    """, unsafe_allow_html=True)
