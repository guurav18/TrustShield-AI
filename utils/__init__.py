"""
TrustShield AI - Utils Package
Re-exports all functions from the root utils.py module so that
`from utils import extract_frames` works whether Python resolves
this package or the sibling utils.py file.
"""
import sys
import os
import importlib.util

# Load the root-level utils.py explicitly (not this package itself)
_utils_py = os.path.join(os.path.dirname(os.path.dirname(__file__)), "utils.py")
_spec = importlib.util.spec_from_file_location("_utils_root", _utils_py)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

# Re-export everything from utils.py
extract_frames = _mod.extract_frames
preprocess_frames = _mod.preprocess_frames
load_dataset = _mod.load_dataset
prepare_frames_for_prediction = _mod.prepare_frames_for_prediction
load_faceforensics_dataset = _mod.load_faceforensics_dataset
crop_face = getattr(_mod, 'crop_face', None)
get_face_cascade = getattr(_mod, 'get_face_cascade', None)
HAS_CV2 = _mod.HAS_CV2

__all__ = [
    "extract_frames",
    "preprocess_frames",
    "load_dataset",
    "prepare_frames_for_prediction",
    "load_faceforensics_dataset",
    "crop_face",
    "get_face_cascade",
    "HAS_CV2",
]

