# Название: Загрузка в Telegram фотографий космоса

Приложение может загружать фотографии с API Nasa и постить их в Telegram

![скрин](https://dvmn.org/media/lessons/space.jpg)


### Окружение: Как установить

* Скачать [этот script](https://github.com/qqJonni/space_photos.git)

**Python 3.11 уже должен быть установлен**. 
Используйте `pip` (или `pip3`, если возникает конфликт с Python2) для установки зависимостей:

**Создаём и активируем виртуальное окружение:**

Для MacOS: Обычно окружение создается командой python3 -m venv имя_окружения; source имя_окружения/bin/activate

Для Windows: C:\> имя_окружения\Scripts\activate.bat


### Зависимости
```properties
pip install -r requirements.txt
```
### Переменные окружения
Создать в корне проекта файл .env и указать:
APOD_TOKEN - токен, который необходимо получить на сайте https://api.nasa.gov
TELEGRAM_TOKEN - токен, который можно получить у BotFather в Telegram


### Запуск

Запуск скриптов выполняется командой:
```properties
python fetch_spacex_images.py <url upload_to> 
```
Эта команда скачивает картинки. Более подробную информацию смотреть здесь - https://github.com/r-spacex/SpaceX-API (url - адрес сайта, upload_to - путь, куда нужно скачать картинки)
```properties
python fetch_nasa_apod_images.py <url upload_to> 
```
Эта команда скачивает картинки. Более подробную информацию смотреть здесь - https://api.nasa.gov/#apod
```properties
python fetch_nasa_epic_images.py <url upload_to> 
```
Эта команда скачивает картинки. Более подробную информацию смотреть здесь - https://api.nasa.gov/#epic
```properties
python space_photos % python telegram_bot.py <seconds>
```
Эта команда запускает телеграм бота, который постит скачанные фотографии, где seconds - целочисленное значение(колличество секунд с которой будут поститься фото)
### Примечания


Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
