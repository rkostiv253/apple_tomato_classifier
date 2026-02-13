import io
import numpy as np
from PIL import Image
from flask import Flask, request, render_template, redirect, url_for
import tensorflow as tf

MODEL_PATH = "apple_tomato_classifier.keras"
IMG_SIZE = (224, 224)

model = tf.keras.models.load_model(MODEL_PATH)

app = Flask(__name__)

def preprocess_image(file_bytes: bytes) -> tf.Tensor:
    img = Image.open(io.BytesIO(file_bytes)).convert("RGB")

    img_tf = tf.convert_to_tensor(np.array(img), dtype=tf.uint8)
    img_tf = tf.image.resize_with_pad(img_tf, IMG_SIZE[0], IMG_SIZE[1])
    img_tf = tf.cast(img_tf, tf.float32)

    x = tf.expand_dims(img_tf, axis=0)

    return x

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/predict")
def predict():
    if "image" not in request.files:
        return redirect(url_for("index"))

    file = request.files["image"]
    if file.filename == "":
        return redirect(url_for("index"))

    x = preprocess_image(file.read())
    prob_tomato = float(model.predict(x, verbose=0)[0][0])

    label = 1 if prob_tomato >= 0.5 else 0

    if label == 0:
        return redirect(url_for("apple_page", prob=prob_tomato))
    return redirect(url_for("tomato_page", prob=prob_tomato))

@app.get("/apple")
def apple_page():
    prob = request.args.get("prob", default=None)
    return render_template("apple.html", prob=prob)

@app.get("/tomato")
def tomato_page():
    prob = request.args.get("prob", default=None)
    return render_template("tomato.html", prob=prob)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
