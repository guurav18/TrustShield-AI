"""
TrustShield AI - Batch Audit Queue Component
Renders multi-video drag-and-drop batch analysis, queue processing status, and CSV export.
"""

import streamlit as st
import tempfile
import os
import pandas as pd
from datetime import datetime
from forensics.crypto_utils import compute_file_sha256


def render_batch_analysis(detector):
    """Render batch audit queue view."""
    st.subheader("📦 Enterprise Multi-Video Batch Audit Queue")
    st.caption("Perform parallel multi-modal triage across bulk media uploads for enterprise security teams.")
    
    batch_files = st.file_uploader(
        "Drag & drop multiple videos to queue",
        type=["mp4", "avi", "mov", "mkv"],
        accept_multiple_files=True,
        key="batch_files_inspector"
    )
    
    if batch_files:
        if st.button("🚀 Launch Parallel Batch Audit Queue", use_container_width=True):
            batch_results = []
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for idx, file in enumerate(batch_files):
                status_text.markdown(f"⏳ **Processing [{idx+1}/{len(batch_files)}]:** `{file.name}`")
                
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
                    tmp.write(file.getbuffer())
                    tmp_p = tmp.name
                    
                file.seek(0)
                f_hash = compute_file_sha256(file.read())
                
                try:
                    res = detector.predict_video(tmp_p, num_frames=10)
                    if res:
                        trust_score = max(2.0, min(99.0, (1.0 - res['prediction']) * 100))
                        batch_results.append({
                            'File Name': file.name,
                            'Verdict': 'DEEPFAKE ⚠️' if res['is_fake'] else 'AUTHENTIC ✅',
                            'Trust Score': f"{trust_score:.1f} / 100",
                            'AI Confidence': f"{res['confidence']:.1f}%",
                            'SHA-256 Checksum': f_hash[:12] + "...",
                            'Timestamp': datetime.now().strftime("%H:%M:%S")
                        })
                finally:
                    if os.path.exists(tmp_p):
                        os.remove(tmp_p)
                        
                progress_bar.progress(int(((idx + 1) / len(batch_files)) * 100))
                
            status_text.empty()
            progress_bar.empty()
            st.success(f"✅ Audit Queue Finished! Processed {len(batch_files)} media files.")
            
            df_b = pd.DataFrame(batch_results)
            st.dataframe(df_b, use_container_width=True)
            
            f_count = sum(1 for r in batch_results if 'DEEPFAKE' in r['Verdict'])
            a_count = len(batch_results) - f_count
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Batch Files", len(batch_results))
            c2.metric("Flagged Deepfakes", f_count, delta=f"{f_count} Threat(s)", delta_color="inverse")
            c3.metric("Verified Authentic", a_count)
            
            st.markdown("---")
            st.download_button(
                label="📥 Export Enterprise Audit Summary (CSV)",
                data=df_b.to_csv(index=False),
                file_name=f"TrustShield_Batch_Audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
    else:
        st.info("👆 Drop multiple video files above to initiate bulk enterprise auditing.")
