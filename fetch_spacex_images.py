import requests
import argparse
from space_photos import upload_image


def fetch_spacex_last_launch(id, upload_to):

    url = f'https://api.spacexdata.com/v5/launches/{id}'

    response = requests.get(url)
    response.raise_for_status()
    content = response.json()
    original_links = content["links"]["flickr"]["original"]

    for url_number, url in enumerate(original_links):
        upload_image(url, upload_to, f'spacex{url_number}.jpeg')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('id', help='Enter id')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id, args.upload_to)
