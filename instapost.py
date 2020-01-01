from instabot import Bot
from dotenv import load_dotenv
import os
from PIL import Image


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((
        img_width - crop_width) // 2,
        (img_height - crop_height) // 2,
        (img_width + crop_width) // 2,
        (img_height + crop_height) // 2))


def save_cropped_all_files():
    all_image_files = os.listdir('images/')
    for file_image in all_image_files:
        image = Image.open(f'images/{file_image}'')
        image_crop = crop_center(image, 1080, 1080)
        image_crop.save('images/{file_image}')


def post_all_photos():
    login = os.getenv('LOGIN_INSTA')
    password = os.getenv('PASS_INSTA')
    bot = Bot()
    bot.login(username=login, password=password)
    images = os.listdir('images')
    for image in images:
        try:
            bot.upload_photo(f'images/{image}', caption='Cosmos!')
            print(f'{image} uploaded')
        except:
            print(f'Файл {image} не был загружен')


def main():
    post_all_photos()

if __name__ == '__main__':
    load_dotenv()
    main()
