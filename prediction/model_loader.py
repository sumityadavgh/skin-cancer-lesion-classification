import os
import numpy as np
from PIL import Image
from django.conf import settings
from ai_edge_litert.interpreter import Interpreter


MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "model",
    "final_efficientnetb0.tflite"
)

interpreter = Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


CLASS_NAMES = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "mel",
    "nv",
    "vasc"
]


print("EfficientNetB0 LiteRT model loaded successfully!")


def predict_image(image):
    image = Image.open(image).convert("RGB")
    image = image.resize((224, 224))

    image_array = np.array(image).astype("float32")
    image_array = np.expand_dims(image_array, axis=0)

    interpreter.set_tensor(
        input_details[0]["index"],
        image_array
    )

    interpreter.invoke()

    predictions = interpreter.get_tensor(
        output_details[0]["index"]
    )

    predicted_index = np.argmax(predictions[0])

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = (
        float(predictions[0][predicted_index]) * 100
    )

    return predicted_class, confidence