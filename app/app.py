from flask import Flask, render_template, request
import socket
import site_image
from keras.models import load_model

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    prediction = None
    image_data = None
    if request.method == 'POST':
        image_data = request.form['imageData']
        image = site_image.get_image_from_data_url(image_data)
        image_array = site_image.prepare_image(image, target=(28, 28))
        predictions = model.predict(image_array)
        prediction = str(predictions)
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html',
                               hostname=host_name, ip=host_ip, prediction=prediction, image_data=image_data)
    except:
        return render_template('error.html')


def init_model():
    global model
    model = load_model('classification_model.h5')
    model._make_predict_function()


if __name__ == "__main__":
    init_model()
    app.run(host='0.0.0.0', port=5000)

