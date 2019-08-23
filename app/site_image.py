from flask import Flask
from PIL import Image, ImageOps, ImageFilter
import base64
import io
import binascii

app = Flask(__name__)


__all__ = ['normalize_image', 'get_data_uri']


def normalize_image(image_data=None):
    if image_data is None:
        raise TypeError('Image data must not be None')

    # The received image data in an PNG file in RGB format, encoded in base 64.
    image_from_data = Image.open(io.BytesIO(binascii.a2b_base64(image_data)))

    # Create a new, all-white image.
    normalized_image = Image.new("RGB", image_from_data.size, "white")
    # Paste the submitted drawing on to it.
    normalized_image.paste(image_from_data, (0, 0), image_from_data)
    # Convert to greyscale
    normalized_image = normalized_image.convert('L')
    # Soften the edges a bit
    normalized_image = normalized_image.filter(ImageFilter.GaussianBlur(radius=1))

    # Resize to MNIST image size.
    normalized_image = normalized_image.resize((28, 28))
    # Invert to match MNIST: white digits on a black background.
    normalized_image = ImageOps.invert(normalized_image)

    return normalized_image


def get_data_uri(image=None):
    if image == None:
        raise TypeError('Image must not be None')

    prefix = 'data:image/png;base64,'
    buffer = io.BytesIO()
    ImageOps.invert(image).save(buffer, format='PNG')
    encoded_image = base64.b64encode(buffer.getvalue())
    return encoded_image.decode('ascii')


