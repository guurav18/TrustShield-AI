"""
TrustShield AI - Cyber Awareness & Digital Privacy Hub Component
Educates users on deepfake detection indicators, privacy defense, Do's & Don'ts, and interactive 10-Question Cyber Quiz.
"""

import streamlit as st

GRAD   = "🎓"
SHIELD = "🛡️"
CHECK  = "✅"
CROSS  = "❌"
WARN   = "⚠️"
LOCK   = "🔒"
EYE    = "👁️"
PHONE  = "📞"
TROPHY = "🏆"
STAR   = "⭐"


# 10 Detailed Awareness Quiz Questions
QUIZ_QUESTIONS = [
    {
        "id": "q1",
        "question": "Q1: You receive a viral video of a politician making a shocking statement. What should be your FIRST action?",
        "options": [
            "A) Immediately forward it to all your WhatsApp groups to inform others",
            "B) Verify the video on official news portals and inspect for lip-sync / blinking artifacts",
            "C) Comment on the video to express your outrage",
            "D) Download and save the video on your phone"
        ],
        "answer_idx": 1,
        "explanation": "Correct! Always verify viral media against trusted news sources and check for visual artifacts like lip desync or lack of blinking before sharing."
    },
    {
        "id": "q2",
        "question": "Q2: An urgent voice call sounding EXACTLY like your family member asks for immediate money via UPI after an accident. What do you do?",
        "options": [
            "A) Immediately transfer the money to help them",
            "B) Disconnect and call your family member directly on their saved phone number or verify with another relative",
            "C) Ask for their UPI PIN",
            "D) Post about it on social media"
        ],
        "answer_idx": 1,
        "explanation": "Correct! AI voice cloning only needs 3 seconds of audio to mimic a voice. Always disconnect and call the person back on their known number."
    },
    {
        "id": "q3",
        "question": "Q3: An unknown number makes a WhatsApp video call. When answered, the caller is silent and records your face. What is the hidden danger?",
        "options": [
            "A) It is just a network connection glitch",
            "B) Scammers can capture your live face video to create a synthetic deepfake clone for fraud",
            "C) It will drain your phone battery",
            "D) Nothing to worry about"
        ],
        "answer_idx": 1,
        "explanation": "Correct! Unknown video calls can be recorded to harvest facial biometrics for deepfake impersonation. Avoid video calls from strangers."
    },
    {
        "id": "q4",
        "question": "Q4: How can you protect your social media photos and videos from being harvested by deepfake generators?",
        "options": [
            "A) Delete all your social media accounts permanently",
            "B) Keep your social media profiles Private, restrict audience access, and avoid uploading raw ultra-HD close-ups",
            "C) Post photos only at night",
            "D) Use black-and-white filters only"
        ],
        "answer_idx": 1,
        "explanation": "Correct! Locking profile privacy prevents automated web crawlers from scraping your face photos to train face-swap models."
    },
    {
        "id": "q5",
        "question": "Q5: A viral third-party AI app promises to show how you will look at age 80 by uploading a selfie. What is the privacy risk?",
        "options": [
            "A) The app might slow down your phone",
            "B) Unverified apps may harvest and store your facial biometric embeddings on unknown overseas servers",
            "C) The photo quality will decrease",
            "D) There is zero risk in using AI avatar apps"
        ],
        "answer_idx": 1,
        "explanation": "Correct! Many free viral face apps store biometric facial templates in their databases without clear privacy consent."
    },
    {
        "id": "q6",
        "question": "Q6: Which of the following is a physical sign of an AI Deepfake video when inspected with the naked eye?",
        "options": [
            "A) The video has background music",
            "B) Unnatural blinking, edge blur around jawline/hairline, and unnatural teeth alignment",
            "C) The video duration is under 1 minute",
            "D) High screen brightness"
        ],
        "answer_idx": 1,
        "explanation": "Correct! Deepfakes often struggle with natural eye blinks, clean jawline borders, and realistic interior mouth/teeth geometry."
    },
    {
        "id": "q7",
        "question": "Q7: A caller claiming to be a bank agent asks you to install AnyDesk or TeamViewer during a video KYC check. Is this safe?",
        "options": [
            "A) Yes, bank agents frequently request remote screen access",
            "B) NO! Never grant screen-sharing access; scammers can view OTPs, banking credentials, and personal data in real time",
            "C) Yes, if they show an official badge on camera",
            "D) Only if your phone battery is full"
        ],
        "answer_idx": 1,
        "explanation": "Correct! Banks NEVER ask for screen-sharing app installation. Screen access allows scammers to steal OTPs and compromise banking apps."
    },
    {
        "id": "q8",
        "question": "Q8: Where should you immediately report deepfake identity theft, cyber extortion, or synthetic video scams in India?",
        "options": [
            "A) Post a tweet on Twitter",
            "B) Report on National Cyber Crime Portal (cybercrime.gov.in) or call National Cyber Helpline 1930",
            "C) Email your phone manufacturer",
            "D) Wait for 30 days"
        ],
        "answer_idx": 1,
        "explanation": "Correct! Helpline 1930 and cybercrime.gov.in are India's official national portals for rapid cyber incident reporting and financial fraud freeze."
    },
    {
        "id": "q9",
        "question": "Q9: How much audio recording of a target person does modern generative AI voice cloning software need to clone a voice?",
        "options": [
            "A) 100 hours of studio recording",
            "B) Just 3 to 5 seconds of clear audio from a phone call or reel",
            "C) 1 full week of continuous listening",
            "D) Voice cloning is impossible"
        ],
        "answer_idx": 1,
        "explanation": "Correct! Advanced neural voice synthesizers can clone pitch, cadence, and tone from just 3-5 seconds of clear sample audio."
    },
    {
        "id": "q10",
        "question": "Q10: What is the single most effective account security setting to prevent hackers from hijacking your social media for identity impersonation?",
        "options": [
            "A) Changing your profile picture weekly",
            "B) Enabling App-Based Two-Factor Authentication (2FA) on all accounts",
            "C) Using your birthdate as password",
            "D) Logging out every night"
        ],
        "answer_idx": 1,
        "explanation": "Correct! 2FA requires an authenticator code even if someone steals your password, blocking 99.9% of automated account takeover attempts."
    }
]


def render_cyber_awareness():
    """Render Cyber Awareness, Digital Safety & 10-Question Privacy Quiz Hub."""
    
    # 1. Hero Awareness Banner
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 50%, rgba(13, 148, 136, 0.25) 100%);
        border: 2px solid rgba(20, 184, 166, 0.5);
        border-radius: 20px;
        padding: 28px 36px;
        margin-bottom: 24px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), inset 0 1px 1px rgba(255, 255, 255, 0.15);
    ">
        <div style="display: flex; align-items: center; gap: 18px; flex-wrap: wrap;">
            <div style="
                font-size: 34px;
                width: 60px;
                height: 60px;
                background: linear-gradient(135deg, rgba(20, 184, 166, 0.3), rgba(56, 189, 248, 0.3));
                border: 2px solid #00F2FE;
                border-radius: 16px;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 0 25px rgba(0, 242, 254, 0.4);
            ">{GRAD}</div>
            <div>
                <h1 style="font-size: 32px; font-weight: 900; background: linear-gradient(90deg, #00F2FE 0%, #38BDF8 50%, #818CF8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; letter-spacing: -0.5px;">
                    Cyber Awareness & Digital Privacy Hub
                </h1>
                <p style="color: #CBD5E1; font-size: 15px; margin-top: 6px; font-weight: 600;">
                    Learn how to spot AI deepfakes, protect your biometric privacy, and take the 10-Question Cyber Security Assessment!
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. DOs and DON'Ts Section
    st.subheader("🛡️ Digital Safety Guide: DOs and DON'Ts (क्या करें और क्या न करें)")
    
    c_do, c_dont = st.columns(2)
    
    with c_do:
        st.markdown(f"""
        <div style="background: rgba(34, 197, 94, 0.08); border: 2px solid #22C55E; border-top: 6px solid #22C55E; padding: 22px; border-radius: 16px; box-shadow: 0 8px 24px rgba(34, 197, 94, 0.15);">
            <h3 style="color: #22C55E; font-size: 20px; font-weight: 900; margin-top: 0;">{CHECK} DOs (क्या करें)</h3>
            <ul style="color: #F8FAFC; font-size: 14px; line-height: 1.9; padding-left: 20px; margin-bottom: 0; font-weight: 500;">
                <li><b>Verify Source Authenticity:</b> Cross-check news & video clips on official news portals before forwarding.</li>
                <li><b>Inspect Visual Artifacts:</b> Look for unnatural blinking, jawline blurring, lighting shifts, and lip desync.</li>
                <li><b>Lock Social Media Profiles:</b> Set profiles to Private to prevent stranger scraping of photos for face-swaps.</li>
                <li><b>Enable 2FA Protection:</b> Secure all email and messaging accounts with App-Based Two-Factor Authentication.</li>
                <li><b>Report Cyber Fraud:</b> Report deepfake extortion or impersonation immediately on <b>Helpline 1930</b> or <a href="https://cybercrime.gov.in" target="_blank" style="color: #00F2FE; font-weight: bold;">cybercrime.gov.in</a>.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with c_dont:
        st.markdown(f"""
        <div style="background: rgba(239, 68, 68, 0.08); border: 2px solid #EF4444; border-top: 6px solid #EF4444; padding: 22px; border-radius: 16px; box-shadow: 0 8px 24px rgba(239, 68, 68, 0.15);">
            <h3 style="color: #EF4444; font-size: 20px; font-weight: 900; margin-top: 0;">{CROSS} DON'Ts (क्या न करें)</h3>
            <ul style="color: #F8FAFC; font-size: 14px; line-height: 1.9; padding-left: 20px; margin-bottom: 0; font-weight: 500;">
                <li><b>DON'T Forward Unverified Viral Media:</b> Never share unconfirmed emotional or political videos on WhatsApp.</li>
                <li><b>DON'T Use Unverified Face-Swap Apps:</b> Avoid viral face-aging or avatar apps that harvest facial biometrics.</li>
                <li><b>DON'T Transfer Money on Voice Calls Alone:</b> Voice cloning takes 3 seconds. Always call back to verify.</li>
                <li><b>DON'T Accept Stranger Video Calls:</b> Unknown video callers can record your face to build synthetic clones.</li>
                <li><b>DON'T Share Screen Access:</b> Never install remote access apps (AnyDesk/TeamViewer) during video calls.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 32px;'></div>", unsafe_allow_html=True)
    
    # 3. How to Spot Deepfakes Checklist
    st.subheader("🔍 Naked-Eye Deepfake Spotting Checklist")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.95); border: 2px solid rgba(56, 189, 248, 0.4); border-radius: 16px; padding: 20px; text-align: center; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);">
            <div style="font-size: 32px; margin-bottom: 8px;">{EYE}</div>
            <div style="font-size: 15px; font-weight: 900; color: #00F2FE;">1. Unnatural Blinking</div>
            <div style="font-size: 13px; color: #CBD5E1; margin-top: 8px; line-height: 1.6;">
                AI deepfakes struggle to match natural blinking cadence or fail to close eyelids fully.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.95); border: 2px solid rgba(56, 189, 248, 0.4); border-radius: 16px; padding: 20px; text-align: center; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);">
            <div style="font-size: 32px; margin-bottom: 8px;">👄</div>
            <div style="font-size: 15px; font-weight: 900; color: #00F2FE;">2. Lip & Teeth Lag</div>
            <div style="font-size: 13px; color: #CBD5E1; margin-top: 8px; line-height: 1.6;">
                Teeth geometry often blurs during speech, and lip movements desync with spoken words.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.95); border: 2px solid rgba(56, 189, 248, 0.4); border-radius: 16px; padding: 20px; text-align: center; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);">
            <div style="font-size: 32px; margin-bottom: 8px;">💡</div>
            <div style="font-size: 15px; font-weight: 900; color: #00F2FE;">3. Lighting & Shadows</div>
            <div style="font-size: 13px; color: #CBD5E1; margin-top: 8px; line-height: 1.6;">
                Check if facial highlights and eye reflections match the direction of background lights.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.95); border: 2px solid rgba(56, 189, 248, 0.4); border-radius: 16px; padding: 20px; text-align: center; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);">
            <div style="font-size: 32px; margin-bottom: 8px;">🔍</div>
            <div style="font-size: 15px; font-weight: 900; color: #00F2FE;">4. Jawline Boundary Blur</div>
            <div style="font-size: 13px; color: #CBD5E1; margin-top: 8px; line-height: 1.6;">
                Inspect hair edges, chin borders, and eyeglasses frames for pixel flickering or smoothing.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 36px;'></div>", unsafe_allow_html=True)

    # 4. Interactive 10-Question Cyber Assessment Quiz Engine
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%);
        border: 2px solid #00F2FE;
        border-radius: 20px;
        padding: 24px 30px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 242, 254, 0.2);
    ">
        <h2 style="color: #00F2FE; font-size: 26px; font-weight: 900; margin: 0; display: flex; align-items: center; gap: 10px;">
            {TROPHY} Interactive 10-Question Cyber Safety Quiz
        </h2>
        <p style="color: #94A3B8; font-size: 14px; margin-top: 6px; margin-bottom: 0;">
            Test your knowledge! Answer all 10 questions below to calculate your Cyber Security Score & earn your Shield Certificate.
        </p>
    </div>
    """, unsafe_allow_html=True)

    user_answers = {}
    
    for idx, q in enumerate(QUIZ_QUESTIONS):
        st.markdown(f"""
        <div style="
            background: rgba(15, 23, 42, 0.85);
            border: 2px solid rgba(56, 189, 248, 0.3);
            border-left: 6px solid #38BDF8;
            border-radius: 16px;
            padding: 20px 24px;
            margin-bottom: 20px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
        ">
            <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; line-height: 1.5;">
                {q['question']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        selected_option = st.radio(
            f"Select your answer for {q['id']}:",
            options=q['options'],
            key=f"radio_{q['id']}",
            index=0,
            label_visibility="collapsed"
        )
        
        selected_idx = q['options'].index(selected_option)
        user_answers[q['id']] = selected_idx
        
        st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    st.markdown("---")

    # Quiz Submission & Score Calculation
    if st.button("🏆 Submit & Calculate Cyber Defense Score", key="btn_submit_quiz", use_container_width=True):
        score = 0
        correct_list = []
        
        for q in QUIZ_QUESTIONS:
            if user_answers[q['id']] == q['answer_idx']:
                score += 1
                correct_list.append(True)
            else:
                correct_list.append(False)
                
        pct = int((score / len(QUIZ_QUESTIONS)) * 100)
        
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
        
        if score >= 8:
            badge_color = "#22C55E"
            rank = "🛡️ CYBER SHIELD SPECIALIST (EXCELLENT)"
        elif score >= 5:
            badge_color = "#F59E0B"
            rank = "⚠️ CYBER AWARE GUARDIAN (GOOD)"
        else:
            badge_color = "#EF4444"
            rank = "❌ HIGH VULNERABILITY RISK (NEEDS IMPROVEMENT)"
            
        st.markdown(f"""
        <div style="
            background: rgba(15, 23, 42, 0.95);
            border: 3px solid {badge_color};
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
        ">
            <div style="font-size: 13px; font-weight: 900; color: #94A3B8; letter-spacing: 1.5px; text-transform: uppercase;">QUIZ SCORE RESULT</div>
            <div style="font-size: 52px; font-weight: 900; color: {badge_color}; margin-top: 6px;">{score} / 10</div>
            <div style="font-size: 20px; font-weight: 900; color: #F8FAFC; margin-top: 4px;">{rank}</div>
            <div style="font-size: 14px; color: #CBD5E1; margin-top: 10px;">Cyber Security Awareness Rating: <b>{pct}%</b></div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
        st.subheader("📝 Detailed Question-by-Question Breakdown")
        
        for idx, q in enumerate(QUIZ_QUESTIONS):
            is_correct = correct_list[idx]
            if is_correct:
                st.success(f"**{q['question']}**\n\n✅ **Correct Answer!** {q['explanation']}")
            else:
                correct_text = q['options'][q['answer_idx']]
                st.error(f"**{q['question']}**\n\n❌ **Incorrect.** Correct Answer: **{correct_text}**\n\n💡 *{q['explanation']}*")

    st.markdown("---")

    # 5. Emergency Helplines Box
    st.subheader("🚨 Emergency Cyber Crime Helplines & Official Reporting")
    
    c_h1, c_h2 = st.columns(2)
    
    with c_h1:
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.9); border: 2px solid #00F2FE; border-radius: 16px; padding: 22px;">
            <div style="font-size: 13px; color: #94A3B8; font-weight: bold;">NATIONAL CYBER CRIME HELPLINE:</div>
            <div style="font-size: 32px; font-weight: 900; color: #00F2FE; margin-top: 4px;">📞 1930</div>
            <div style="font-size: 12px; color: #CBD5E1; margin-top: 6px;">Toll-free emergency helpline for reporting financial cyber fraud & identity crimes in India.</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c_h2:
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.9); border: 2px solid #38BDF8; border-radius: 16px; padding: 22px;">
            <div style="font-size: 13px; color: #94A3B8; font-weight: bold;">OFFICIAL PORTALS:</div>
            <div style="margin-top: 8px;"><a href="https://cybercrime.gov.in" target="_blank" style="color: #00F2FE; font-size: 16px; font-weight: 800;">👉 cybercrime.gov.in</a></div>
            <div style="margin-top: 4px;"><a href="https://www.cert-in.org.in" target="_blank" style="color: #818CF8; font-size: 16px; font-weight: 800;">👉 cert-in.org.in</a></div>
        </div>
        """, unsafe_allow_html=True)
