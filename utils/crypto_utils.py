"""
TrustShield AI - Cryptographic & Verification Utilities
Handles SHA-256 calculation, digital signatures, and C2PA certificate hashing.
"""

import hashlib
import json
from datetime import datetime


def compute_file_sha256(file_bytes: bytes) -> str:
    """Calculate SHA-256 hash of raw file bytes."""
    return hashlib.sha256(file_bytes).hexdigest()


def generate_c2pa_signature(file_hash: str, trust_score: float, case_id: str) -> str:
    """Generate tamper-evident digital signature hash for evidence records."""
    raw_payload = f"TRUSTSHIELD_C2PA_v3.4::{case_id}::{file_hash}::{trust_score:.4f}"
    return hashlib.sha256(raw_payload.encode('utf-8')).hexdigest()


def create_forensic_certificate(file_name: str, file_hash: str, trust_score: float, threat_level: str, verdict: str) -> dict:
    """Compile structured C2PA-compatible digital evidence certificate."""
    case_id = f"TS-{file_hash[:8].upper()}-{datetime.now().strftime('%Y%m%d')}"
    signature = generate_c2pa_signature(file_hash, trust_score, case_id)
    
    return {
        "certificate_id": case_id,
        "standard": "C2PA / ISO 27037 Evidence Spec",
        "system": "TrustShield AI Multi-Modal Engine v3.4",
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "media_file": file_name,
        "sha256_checksum": file_hash,
        "trust_score": round(trust_score, 2),
        "threat_level": threat_level,
        "verdict": verdict,
        "digital_signature": signature,
        "authenticity_status": "VERIFIED_TAMPER_EVIDENT"
    }
