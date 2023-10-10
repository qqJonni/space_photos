import argparse
import os
import requests
from space_photos import upload_image


def upload_epic_nasa_photo(token, upload_to):

    url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=Qx8bePy2Hxre3Rj1VoyfmmKfl3gu71A5nHnfgeHz'
    headers = {"Auth": token}
    payload = {
        'api_key': token
    }

    response = requests.get(url)
    response.raise_for_status()
    content = response.json()
    combined_data = [(entry['date'], entry['image']) for entry in content if 'date' in entry and 'image' in entry]
    # original_dates = [entry['date'] for entry in content if 'date' in entry]
    # original_image = [entry['image'] for entry in content if 'image' in entry]

    for url_number, (date, image) in enumerate(combined_data):
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'
        image_response = requests.get(image_url, headers=headers, params=payload)
        filename = os.path.join(upload_to, f'epic_photo_{url_number}.png')
        with open(filename, 'wb') as file:
            file.write(image_response.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скачиваем фото spacex')
    parser.add_argument('token', help='Enter your token')
    parser.add_argument('upload_to', help='Enter directory to upload')
    args = parser.parse_args()
    upload_epic_nasa_photo(args.token, args.upload_to)
