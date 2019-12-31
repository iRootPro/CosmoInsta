import requests
import os
import argparse


def get_image(url, filename):

    images_path = f'./images/{filename}'
    directory = os.path.dirname(images_path)
    os.makedirs(directory, exist_ok=True)

    response = requests.get(url, verify=True)
    response.raise_for_status()

    with open(images_path, 'wb') as file:
        file.write(response.content)


def get_links_from_habble(id_image):
    url = f'https://hubblesite.org/api/v3/image/{id_image}'
    response = requests.get(url, verify=True)
    response.raise_for_status()
    image_files = response.json()['image_files']
    links = []
    for image in image_files:
        links.append(f"https:{image['file_url']}")
    return links


def get_exphansion_image(link):
    extension = os.path.splitext(link)
    return extension[1] 


def fetch_habble_images():
    link = get_links_from_habble()[-1]
    extension = get_exphansion_image(link)
    image_id = 1
    filename = str(image_id) + extension 
    get_image(link, filename)


def get_id_image_from_habble_collection(collection):
    url = 'https://hubblesite.org/api/v3/images'

    payload = {
            'collection_name': collection,
            'page': 'all'
            }
    response = requests.get(url, params=payload, verify=True)
    response.raise_for_status()
    ids_image = []
    ids = response.json()
    for i in ids:
        ids_image.append(i['id'])
    return ids_image


def download_all_images_from_collection(collection):
    ids = get_id_image_from_habble_collection(collection)
    links_images = []
    for id_image in ids:
        link = get_links_from_habble(id_image)[-1]
        filename = str(id_image) + '.' + get_exphansion_image(link)
        get_image(link, filename)


def main():
    parser = argparse.ArgumentParser(
        description='Скрипт, который скачивает изображения
        из репозитариев hubble по указанной коллекции')
    parser.add_argument(
        'collect', help='Укажите название коллекции,
        например: wallpaper, news, spacecraft,
        holiday_cards, printshop, stsci_gallery')
    args = parser.parse_args()
    collection = args.collect
    download_all_images_from_collection(collection)

if __name__ == '__main__':
    main()
