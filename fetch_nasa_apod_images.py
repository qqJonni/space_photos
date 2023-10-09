import argparse
import json
import os
import requests

from dotenv import load_dotenv, find_dotenv


IMAGES_COUNT = 30


def upload_apod_nasa_images(url, upload_to):

    payload = {
        'count': IMAGES_COUNT,
        'api_key': token
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    format_json = json.loads(response.content)

    original_links = [entry['hdurl'] for entry in format_json if 'hdurl' in entry]

    for url_number, url in enumerate(original_links):
        image_response = requests.get(url)

        filename = os.path.join(upload_to, f'nasa_apod_{url_number}.jpeg')
        with open(filename, 'wb') as file:
            file.write(image_response.content)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    token = os.environ.get('APOD_TOKEN')
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    upload_apod_nasa_images('https://api.nasa.gov/planetary/apod', args.upload_to)
