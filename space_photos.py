import os
import requests
from urllib.parse import urlparse


def upload_image(url, upload_to, filename):
    image_response = requests.get(url)
    filename = os.path.join(upload_to, filename)
    with open(filename, 'wb') as file:
        file.write(image_response.content)


def get_file_format(url):
    url = url

    res = os.path.splitext(url)
    file_format = urlparse(res[1])

    return file_format.path
