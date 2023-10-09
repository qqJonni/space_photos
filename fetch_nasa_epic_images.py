import argparse
import json
import os
import requests

from dotenv import load_dotenv, find_dotenv


def upload_epic_nasa_photo(url, upload_to):

    url = f'{url}{token}'
    response = requests.get(url)
    data_json = json.loads(response.content)
    original_dates = [entry['date'] for entry in data_json if 'date' in entry]
    original_image = [entry['image'] for entry in data_json if 'image' in entry]

    original_links = []
    for date, image in zip(original_dates, original_image):
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png?api_key={token}'
        original_links.append(image_url)

    for url_number, url in enumerate(original_links):
        filename = os.path.join(upload_to, f'epic_photo_{url_number}.png')
        with open(filename, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    token = os.environ.get('APOD_TOKEN')
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('url', help='Enter url', default=f'https://api.nasa.gov/EPIC/api/natural/images?api_key={token}')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    upload_epic_nasa_photo(args.url, args.upload_to)
