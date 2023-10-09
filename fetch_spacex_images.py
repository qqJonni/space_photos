import requests
import json
import os
import argparse

from dotenv import load_dotenv, find_dotenv


def fetch_spacex_last_launch(url, upload_to):
    url = url
    response = requests.get(url)
    response.raise_for_status()

    data_json = json.loads(response.content)

    original_links = data_json["links"]["flickr"]["original"]

    for url_number, url in enumerate(original_links):
        filename = os.path.join(upload_to, f'spacex{url_number}.jpeg')
        with open(filename, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    token = os.environ.get('APOD_TOKEN')
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('url', help='Enter url', default='https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.url, args.upload_to)
