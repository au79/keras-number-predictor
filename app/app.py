from flask import Flask, render_template, request
import socket

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    prediction = None
    image_data = None
    if request.method == 'POST':
        prediction = '0'
        image_data = request.form['imageData']

    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html',
                               hostname=host_name, ip=host_ip, prediction=prediction, image_data=image_data)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
