import os
import tensorflow as tf
from django.conf import settings


MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "model",
    "final_efficientnetb0.keras"
)

model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "mel",
    "nv",
    "vasc"
]

print("EfficientNetB0 model loaded successfully!")

from PIL import Image
import numpy as np


def predict_image(image):
    # Convert uploaded Django file into a Pillow image
    image = Image.open(image).convert("RGB")

    # Resize image to the same size used during training
    image = image.resize((224, 224))

    # Convert image to NumPy array
    image_array = np.array(image).astype("float32")

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # Make prediction
    predictions = model.predict(image_array, verbose=0)

    # Get the class with highest probability
    predicted_index = np.argmax(predictions[0])

    # Get class name
    predicted_class = CLASS_NAMES[predicted_index]

    # Get confidence
    confidence = float(predictions[0][predicted_index]) * 100

    return predicted_class, confidence