import argparse
import requests
from space_photos import upload_image
from dotenv import load_dotenv, find_dotenv
import os


def upload_epic_nasa_photo(token, upload_to):

    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    headers = {"Auth": token}
    payload = {
        'api_key': token
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    content = response.json()
    original_links = [(entry['date'], entry['image']) for entry in content if 'date' in entry and 'image' in entry]

    for url_number, (date, image) in enumerate(original_links):
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'
        image_response = requests.get(image_url, headers=headers, params=payload)
        upload_image(image_response.url, upload_to, f'epic_photo_{url_number}.png')


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    token = os.environ.get('APOD_TOKEN')
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    upload_epic_nasa_photo(token, args.upload_to)
