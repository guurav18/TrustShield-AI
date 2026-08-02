"""
Configuration file for TrustShield AI
Modify these settings to customize the system
"""

# ============================================================
# PATHS
# ============================================================
DATASET_PATH = "dataset"
MODEL_PATH = "models/deepfake_model.h5"
TRAINING_HISTORY_PATH = "training_history.png"


# ============================================================
# FRAME EXTRACTION SETTINGS
# ============================================================
# Number of frames to extract per video
FRAMES_PER_VIDEO = 10

# Target frame size (will be resized to this)
FRAME_HEIGHT = 128
FRAME_WIDTH = 128


# ============================================================
# MODEL SETTINGS
# ============================================================
# Use lightweight model (faster but potentially less accurate)
USE_LIGHT_MODEL = False

# CNN Architecture parameters (only if building custom model)
CONV_LAYERS = [
    {"filters": 32, "kernel_size": (3, 3)},
    {"filters": 64, "kernel_size": (3, 3)},
    {"filters": 128, "kernel_size": (3, 3)}
]
DENSE_UNITS = 128
DROPOUT_RATE = 0.5


# ============================================================
# TRAINING SETTINGS
# ============================================================
# Number of training epochs
EPOCHS = 20

# Batch size
BATCH_SIZE = 32

# Validation split (0.2 = 20% validation, 80% training)
VALIDATION_SPLIT = 0.2

# Learning rate for Adam optimizer
LEARNING_RATE = 0.001

# Maximum videos per class to load (None = load all)
MAX_VIDEOS_PER_CLASS = None  # Set to 5 for quick testing


# ============================================================
# PREDICTION SETTINGS
# ============================================================
# Confidence threshold (0-1)
# Predictions > 0.5 = FAKE
# Predictions <= 0.5 = REAL
PREDICTION_THRESHOLD = 0.5

# Number of frames to analyze during prediction
PREDICTION_FRAMES = 10


# ============================================================
# STREAMLIT UI SETTINGS
# ============================================================
# Page title
STREAMLIT_PAGE_TITLE = "TrustShield AI - Deepfake Detector"

# Page icon
STREAMLIT_PAGE_ICON = "🛡️"

# Layout
STREAMLIT_LAYOUT = "centered"

# Maximum upload file size (in MB)
MAX_UPLOAD_SIZE_MB = 500


# ============================================================
# LOGGING & DEBUG
# ============================================================
# Verbose output during training
VERBOSE_TRAINING = True

# Print frame-by-frame predictions
VERBOSE_PREDICTIONS = False


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_frame_size():
    """Get frame size as tuple (height, width)"""
    return (FRAME_HEIGHT, FRAME_WIDTH)


def get_model_config():
    """Get model configuration dictionary"""
    return {
        "use_light_model": USE_LIGHT_MODEL,
        "frame_size": get_frame_size(),
        "dropout_rate": DROPOUT_RATE,
        "dense_units": DENSE_UNITS
    }


def get_training_config():
    """Get training configuration dictionary"""
    return {
        "epochs": EPOCHS,
        "batch_size": BATCH_SIZE,
        "validation_split": VALIDATION_SPLIT,
        "learning_rate": LEARNING_RATE,
        "max_videos": MAX_VIDEOS_PER_CLASS
    }


def get_prediction_config():
    """Get prediction configuration dictionary"""
    return {
        "threshold": PREDICTION_THRESHOLD,
        "frames": PREDICTION_FRAMES,
        "frame_size": get_frame_size()
    }


# ============================================================
# PRESETS (uncomment to use)
# ============================================================

# For quick testing with limited data:
# EPOCHS = 5
# MAX_VIDEOS_PER_CLASS = 3
# USE_LIGHT_MODEL = True

# For best accuracy (requires more data):
# EPOCHS = 50
# BATCH_SIZE = 16
# FRAMES_PER_VIDEO = 20

# For GPU training (faster):
# BATCH_SIZE = 64
