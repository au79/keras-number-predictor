from flask import Flask, render_template, request
import socket
import site_image
from keras.models import load_model
import numpy as np


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    prediction = None
    image_data = None
    image = None
    if request.method == 'POST':
        # Get the base64-encoded image data.
        image_data = request.form['imageData']
        # Convert it to a PIL Image object, in the correct size and in greyscale.
        image = site_image.normalize_image(image_data)
        # Extract and normalize the pixel data
        pixel_data = np.array(image.getdata()) / 255
        # Reshape the pixel data to match the model's expected input.
        pixel_data = pixel_data.reshape(1, 28, 28, 1)

        predictions = model.predict(pixel_data)
        prediction = str(predictions.argmax())


        image_data = site_image.get_data_uri(image)

    try:
        return render_template('index.html', prediction=prediction, image_data=image_data)
    except Exception as e:
        app.logger.info(e.__class__.__name__ + ': ' + str(e))
        return render_template('error.html', exception=e)


def init_model():
    global model
    model = load_model('convolutional_model.h5')
    model._make_predict_function()


if __name__ == "__main__":
    init_model()
    app.run(host='0.0.0.0', port=5000)

