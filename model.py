"""
Model architecture for TrustShield AI Deepfake Detection System
Simple CNN for binary classification (Real vs Fake)
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def build_model(input_shape=(128, 128, 3)):
    """
    Build a simple CNN model for deepfake detection.
    
    Architecture:
    - Conv2D (32 filters) → ReLU → MaxPooling
    - Conv2D (64 filters) → ReLU → MaxPooling
    - Conv2D (128 filters) → ReLU → MaxPooling
    - Flatten → Dense (128) → Dropout → Dense (1, sigmoid)
    
    Args:
        input_shape (tuple): Input shape (height, width, channels)
    
    Returns:
        keras.Model: Compiled model ready for training
    """
    model = keras.Sequential([
        # First Conv Block
        layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        
        # Second Conv Block
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        
        # Third Conv Block
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        
        # Flatten and Dense Layers
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        
        # Output Layer (Binary Classification)
        layers.Dense(1, activation='sigmoid')
    ])
    
    # Compile the model
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=['accuracy', keras.metrics.Precision(), keras.metrics.Recall()]
    )
    
    return model


def build_model_light(input_shape=(128, 128, 3)):
    """
    Build a lighter version of the model (faster training for testing).
    Useful for quick prototyping.
    
    Args:
        input_shape (tuple): Input shape (height, width, channels)
    
    Returns:
        keras.Model: Compiled model
    """
    model = keras.Sequential([
        layers.Conv2D(16, (3, 3), activation='relu', padding='same', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    return model
