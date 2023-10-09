import requests
import json
import os
import argparse


def fetch_spacex_last_launch(url, upload_to):

    response = requests.get(url)
    response.raise_for_status()

    format_json = json.loads(response.content)

    original_links = format_json["links"]["flickr"]["original"]

    for url_number, url in enumerate(original_links):
        image_response = requests.get(url)
        filename = os.path.join(upload_to, f'spacex{url_number}.jpeg')
        with open(filename, 'wb') as file:
            file.write(image_response.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    fetch_spacex_last_launch('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a', args.upload_to)
