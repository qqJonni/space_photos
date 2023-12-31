import argparse
import time
import telegram
import os
import random
from dotenv import load_dotenv, find_dotenv


def get_images_from_folder(folder_path):
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                image_files.append(os.path.join(root, file))
    return image_files


def send_photos(chat_id, token, seconds):
    bot = telegram.Bot(token)
    folder_path = "images"
    images = get_images_from_folder(folder_path)
    random_images = random.shuffle(images)

    while True:
        for image in images:
            with open(image, 'rb') as file:
                bot.send_photo(chat_id, file)
            time.sleep(seconds)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    token = os.environ.get('TELEGRAM_TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    parser = argparse.ArgumentParser(description='start telegram bot')
    parser.add_argument('seconds', type=int, help='Целочисленный аргумент', default=14400)
    args = parser.parse_args()
    send_photos(chat_id, token, args.seconds)

