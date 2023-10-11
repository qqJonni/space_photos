import argparse
import requests
from space_photos import upload_image
from dotenv import load_dotenv, find_dotenv
import os


IMAGES_COUNT = 30


def upload_apod_nasa_images(token, upload_to):

    headers = {"Auth": token}
    payload = {
        'count': IMAGES_COUNT,
        'api_key': token
    }

    response = requests.get(f'https://api.nasa.gov/planetary/apod', headers=headers, params=payload)
    response.raise_for_status()
    content = response.json()
    original_links = [entry['hdurl'] for entry in content if 'hdurl' in entry]

    for url_number, url in enumerate(original_links):
        upload_image(url, upload_to, f'nasa_apod_{url_number}.jpeg')


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    token = os.environ.get('APOD_TOKEN')
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    upload_apod_nasa_images(token, args.upload_to)
