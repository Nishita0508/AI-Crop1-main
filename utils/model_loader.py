"""
utils/model_loader.py
Loads the trained TensorFlow disease detection model and the
Scikit-learn crop recommendation model once at startup, and
provides prediction helper functions.
"""

import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image

from config import Config

# ----------------------------
# Load models once (singleton pattern)
# ----------------------------
_disease_model = None
_crop_model = None


def get_disease_model():
    global _disease_model
    if _disease_model is None:
        _disease_model = load_model(Config.DISEASE_MODEL_PATH)
    return _disease_model


def get_crop_model():
    global _crop_model
    if _crop_model is None:
        with open(Config.CROP_MODEL_PATH, "rb") as f:
            _crop_model = pickle.load(f)
    return _crop_model


def predict_disease(image_path: str):
    """
    Predict plant disease from an image file path.
    Returns (disease_name: str, confidence: float)
    """
    model = get_disease_model()

    img = keras_image.load_img(image_path, target_size=Config.DISEASE_IMG_SIZE)
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predictions = model.predict(img_array)
    predicted_index = int(np.argmax(predictions[0]))
    confidence = float(np.max(predictions[0]) * 100)

    if predicted_index < len(Config.DISEASE_CLASSES):
        disease_name = Config.DISEASE_CLASSES[predicted_index]
    else:
        disease_name = "Unknown"

    return disease_name, round(confidence, 2)


def predict_crop(features: dict):
    """
    Predict recommended crop using N, P, K, temperature, humidity, ph, rainfall.
    Returns crop_name: str
    """
    model = get_crop_model()

    input_array = np.array([[
        features["N"],
        features["P"],
        features["K"],
        features["temperature"],
        features["humidity"],
        features["ph"],
        features["rainfall"],
    ]])

    prediction = model.predict(input_array)
    crop_name = str(prediction[0])
    return crop_name
