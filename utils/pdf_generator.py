"""
TrustShield AI - Forensic PDF & HTML Report Generator
Compiles evidence-ready forensic reports for legal, journalistic, and security investigations.
"""

from datetime import datetime
import json


def generate_forensic_html_report(cert_data: dict, ai_findings: list, attack_probs: dict) -> str:
    """Generate professional evidentiary HTML report string suitable for viewing or printing to PDF."""
    
    findings_rows = ""
    for f in ai_findings:
        status_color = "#ef4444" if f['status'] in ['CRITICAL', 'HIGH'] else "#22c55e"
        findings_rows += f"""
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #334155;">{f['icon']} {f['finding']}</td>
            <td style="padding: 10px; border-bottom: 1px solid #334155; font-weight: bold; color: {status_color};">{f['status']}</td>
            <td style="padding: 10px; border-bottom: 1px solid #334155; font-weight: bold;">{f['confidence']:.1f}%</td>
        </tr>
        """

    attack_rows = ""
    for k, v in attack_probs.items():
        attack_rows += f"""
        <tr>
            <td style="padding: 8px; border-bottom: 1px solid #334155;">{k}</td>
            <td style="padding: 8px; border-bottom: 1px solid #334155; font-weight: bold;">{v:.1f}%</td>
        </tr>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>TrustShield AI Forensic Audit Report - {cert_data['certificate_id']}</title>
        <style>
            body {{
                background-color: #0b1020;
                color: #e2e8f0;
                font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
                margin: 0;
                padding: 40px;
            }}
            .report-box {{
                max-width: 900px;
                margin: 0 auto;
                background-color: #131a2e;
                border: 1px solid #38bdf8;
                border-radius: 16px;
                padding: 40px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.8);
            }}
            .header {{
                border-bottom: 2px solid #38bdf8;
                padding-bottom: 20px;
                margin-bottom: 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            .title {{
                color: #00f2fe;
                font-size: 28px;
                font-weight: 800;
                margin: 0;
            }}
            .meta-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
                background-color: #0b1020;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 30px;
                border: 1px solid #1e293b;
            }}
            .meta-item {{
                font-size: 13px;
            }}
            .meta-label {{
                color: #94a3b8;
                font-weight: 600;
                text-transform: uppercase;
                font-size: 11px;
            }}
            .meta-val {{
                color: #f8fafc;
                font-weight: 700;
                font-size: 15px;
                margin-top: 4px;
            }}
            .verdict-banner {{
                background: {'linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(153, 27, 27, 0.4))' if cert_data['verdict'] == 'DEEPFAKE MANIPULATION DETECTED' else 'linear-gradient(135deg, rgba(34, 197, 94, 0.2), rgba(20, 83, 45, 0.4))'};
                border: 2px solid {'#ef4444' if cert_data['verdict'] == 'DEEPFAKE MANIPULATION DETECTED' else '#22c55e'};
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 30px;
                text-align: center;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 30px;
            }}
            th {{
                background-color: #0b1020;
                color: #38bdf8;
                text-align: left;
                padding: 12px;
                font-size: 12px;
                text-transform: uppercase;
            }}
            .footer-sig {{
                border-top: 1px dashed #334155;
                padding-top: 20px;
                margin-top: 40px;
                font-size: 11px;
                color: #64748b;
                word-break: break-all;
            }}
        </style>
    </head>
    <body>
        <div class="report-box">
            <div class="header">
                <div>
                    <h1 class="title">🛡️ TrustShield AI</h1>
                    <div style="color: #94a3b8; font-size: 14px;">Digital Forensic Evidence & Audit Report</div>
                </div>
                <div style="text-align: right; color: #38bdf8; font-weight: bold; font-size: 16px;">
                    CASE ID: {cert_data['certificate_id']}
                </div>
            </div>

            <div class="verdict-banner">
                <h2 style="margin: 0; color: {'#ef4444' if cert_data['verdict'] == 'DEEPFAKE MANIPULATION DETECTED' else '#22c55e'};">
                    {cert_data['verdict']}
                </h2>
                <div style="font-size: 24px; font-weight: 900; margin-top: 6px;">
                    Trust Score: {cert_data['trust_score']} / 100 ({cert_data['threat_level']})
                </div>
            </div>

            <div class="meta-grid">
                <div class="meta-item">
                    <div class="meta-label">Target Media File</div>
                    <div class="meta-val">{cert_data['media_file']}</div>
                </div>
                <div class="meta-item">
                    <div class="meta-label">SHA-256 Checksum</div>
                    <div class="meta-val" style="font-size: 12px; word-break: break-all;">{cert_data['sha256_checksum']}</div>
                </div>
                <div class="meta-item">
                    <div class="meta-label">Analysis Timestamp (UTC)</div>
                    <div class="meta-val">{cert_data['timestamp_utc']}</div>
                </div>
                <div class="meta-item">
                    <div class="meta-label">Forensic Engine</div>
                    <div class="meta-val">{cert_data['system']}</div>
                </div>
            </div>

            <h3 style="color: #38bdf8; border-bottom: 1px solid #1e293b; padding-bottom: 8px;">🔬 Detailed AI Anomaly Findings</h3>
            <table>
                <thead>
                    <tr>
                        <th>Forensic Vector</th>
                        <th>Status</th>
                        <th>Confidence</th>
                    </tr>
                </thead>
                <tbody>
                    {findings_rows}
                </tbody>
            </table>

            <h3 style="color: #38bdf8; border-bottom: 1px solid #1e293b; padding-bottom: 8px;">🎭 Attack Vector Classification</h3>
            <table>
                <thead>
                    <tr>
                        <th>Attack Category</th>
                        <th>Estimated Probability</th>
                    </tr>
                </thead>
                <tbody>
                    {attack_rows}
                </tbody>
            </table>

            <div class="footer-sig">
                <div><b>C2PA Cryptographic Evidence Signature:</b></div>
                <div>{cert_data['digital_signature']}</div>
                <div style="margin-top: 8px;">Verified by TrustShield AI Enterprise Infrastructure. ISO 27037 Digital Forensics Compliant.</div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content
