import argparse
import json
import os
import requests

from dotenv import load_dotenv, find_dotenv


def upload_apod_nasa_images(url, upload_to):

    url = url
    response = requests.get(f'{url}?count=30&api_key={token}')
    response.raise_for_status()

    data_json = json.loads(response.content)

    original_links = [entry['hdurl'] for entry in data_json if 'hdurl' in entry]

    for url_number, url in enumerate(original_links):
        filename = os.path.join(upload_to, f'nasa_apod_{url_number}.jpeg')
        with open(filename, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    token = os.environ.get('APOD_TOKEN')
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('url', help='Enter url', default='https://api.nasa.gov/planetary/apod')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    upload_apod_nasa_images(args.url, args.upload_to)
