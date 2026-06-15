"""
config.py
Centralized configuration for the Flask application.
"""

import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret-key-in-production")

    # Upload settings
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB max upload size

    # Model paths
    DISEASE_MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "disease_model.h5")
    CROP_MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "crop_model.pkl")

    # Disease class labels (update to match your trained model's output order)
    DISEASE_CLASSES = [
    "Apple - Apple Scab",
    "Apple - Black Rot",
    "Apple - Cedar Apple Rust",
    "Apple - Healthy",
    "Bell Pepper - Bacterial Spot",
    "Bell Pepper - Healthy",
    "Cherry - Healthy",
    "Cherry - Powdery Mildew",
    "Corn (Maize) - Cercospora Leaf Spot",
    "Corn (Maize) - Common Rust",
    "Corn (Maize) - Healthy",
    "Corn (Maize) - Northern Leaf Blight",
    "Grape - Black Rot",
    "Grape - Esca (Black Measles)",
    "Grape - Healthy",
    "Grape - Leaf Blight",
    "Peach - Bacterial Spot",
    "Peach - Healthy",
    "Potato - Early Blight",
    "Potato - Healthy",
    "Potato - Late Blight",
    "Strawberry - Healthy",
    "Strawberry - Leaf Scorch",
    "Tomato - Bacterial Spot",
    "Tomato - Early Blight",
    "Tomato - Healthy",
    "Tomato - Late Blight",
    "Tomato - Septoria Leaf Spot",
    "Tomato - Yellow Leaf Curl Virus",
]

    # Crop recommendation model input image size (for disease model)
    DISEASE_IMG_SIZE = (224, 224)

    # Session settings
    SESSION_PERMANENT = False
