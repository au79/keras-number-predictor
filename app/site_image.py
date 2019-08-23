from flask import Flask
from PIL import Image, ImageOps
import io, binascii
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import numpy as np

app = Flask(__name__)


__all__ = ['get_image_from_data_url', 'prepare_image']


def get_image_from_data_url(image_data=None):
    if image_data is None:
        raise TypeError('Image data must not be None')

    file_bytes = io.BytesIO(binascii.a2b_base64(image_data))
    image = Image.open(file_bytes)

    # if the image mode is not RGB, convert it
    if image.mode != "L":
        image = image.convert("L")
    
    return ImageOps.invert(image)


def prepare_image(image, target):
    # resize the input image and preprocess it
    image = image.resize(target)
    image_array = img_to_array(image)
    image_array = np.expand_dims(image, axis=0)
    image_array = imagenet_utils.preprocess_input(image_array)
    app.logger.info(image_array)

    pixel_count = image_array.shape[1] * image_array.shape[2]
    image_array = image_array.reshape(image_array.shape[0], pixel_count)

    # return the processed image
    return image_array
