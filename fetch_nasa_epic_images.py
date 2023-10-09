import argparse
import json
import os
import requests

from dotenv import load_dotenv, find_dotenv


def upload_epic_nasa_photo(url, upload_to):

    payload = {
        'api_key': token
    }

    response = requests.get(url)
    response.raise_for_status()
    format_json = json.loads(response.content)
    original_dates = [entry['date'] for entry in format_json if 'date' in entry]
    original_image = [entry['image'] for entry in format_json if 'image' in entry]

    for url_number, (date, image) in enumerate(zip(original_dates, original_image)):
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'
        image_response = requests.get(image_url, params=payload)
        filename = os.path.join(upload_to, f'epic_photo_{url_number}.png')
        with open(filename, 'wb') as file:
            file.write(image_response.content)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    token = os.environ.get('APOD_TOKEN')
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    upload_epic_nasa_photo('https://api.nasa.gov/EPIC/api/natural/images?api_key=Qx8bePy2Hxre3Rj1VoyfmmKfl3gu71A5nHnfgeHz', args.upload_to)
