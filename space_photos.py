import os
import requests
from urllib.parse import urlparse


def upload_image(url, upload_to):
    filename = os.path.join(upload_to, 'hubble.jpeg')
    url = url
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb')as file:
        file.write(response.content)


def get_file_format(url):
    url = url

    res = os.path.splitext(url)
    file_format = urlparse(res[1])

    return file_format.path
