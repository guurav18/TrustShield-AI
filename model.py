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


def build_transfer_model(model_type='mobilenet', input_shape=(224, 224, 3), learning_rate=1e-3):
    """
    Build a Transfer Learning model (MobileNetV2 or ResNet50V2) with pre-trained ImageNet weights.
    
    Args:
        model_type (str): 'mobilenet', 'resnet', or 'efficientnet'
        input_shape (tuple): Input shape (height, width, channels)
        learning_rate (float): Initial learning rate
        
    Returns:
        tuple: (model, base_model)
    """
    if model_type.lower() == 'resnet':
        base_model = tf.keras.applications.ResNet50V2(
            input_shape=input_shape,
            include_top=False,
            weights='imagenet'
        )
    elif model_type.lower() == 'efficientnet':
        base_model = tf.keras.applications.EfficientNetB0(
            input_shape=input_shape,
            include_top=False,
            weights=None
        )
    else:
        # Default MobileNetV2 - fast, accurate & lightweight
        base_model = tf.keras.applications.MobileNetV2(
            input_shape=input_shape,
            include_top=False,
            weights='imagenet'
        )

    
    # Freeze base model initially
    base_model.trainable = False
    
    inputs = layers.Input(shape=input_shape)
    x = base_model(inputs, training=False)
    x = layers.GlobalAveragePooling2D(name="avg_pool")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.4)(x)
    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(1, activation='sigmoid', name="classifier")(x)
    
    model = keras.Model(inputs=inputs, outputs=outputs, name=f"trustshield_{model_type}")
    
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss='binary_crossentropy',
        metrics=['accuracy', keras.metrics.Precision(name='precision'), keras.metrics.Recall(name='recall')]
    )
    return model, base_model



def unfreeze_for_finetuning(model, base_model, num_unfreeze_layers=20, fine_tune_lr=1e-5):
    """
    Unfreeze top layers of base_model for stage 2 fine-tuning with low learning rate.
    """
    base_model.trainable = True
    
    for layer in base_model.layers[:-num_unfreeze_layers]:
        layer.trainable = False
        
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=fine_tune_lr),
        loss='binary_crossentropy',
        metrics=['accuracy', keras.metrics.Precision(name='precision'), keras.metrics.Recall(name='recall')]
    )
    return model

