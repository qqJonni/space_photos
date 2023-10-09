import argparse
import time
import telegram
import os
from dotenv import load_dotenv, find_dotenv
import random


def get_images_from_folder(folder_path):
    image_files = []
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                    image_files.append(os.path.join(root, file))
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    return image_files


def send_photo(seconds):
    folder_path = "images"
    images = get_images_from_folder(folder_path)
    random_images = random.shuffle(images)

    while True:
        for image in images:
            bot.send_photo('1500316931', open(f'{image}', 'rb'))
            time.sleep(seconds)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    bot = telegram.Bot(os.environ.get('TELEGRAM_TOKEN'))
    parser = argparse.ArgumentParser(description='start telegram bot')
    parser.add_argument('seconds', type=int, help='Целочисленный аргумент', default=14400)
    args = parser.parse_args()
    send_photo(args.seconds)

