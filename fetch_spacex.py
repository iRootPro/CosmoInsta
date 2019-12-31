import requests
import os

def get_links(url):
    response = requests.get(url, verify = True)
    response.raise_for_status()
    links = response.json()['links']['flickr_images']
    return links

def get_image(url, filename):

    images_path = f'./images/{filename}'
    directory = os.path.dirname(images_path)

    try:
        os.stat(directory)
    except:
        os.mkdir(directory)

    response = requests.get(url, verify = True)
    response.raise_for_status()

    with open(images_path, 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch():
    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
    links = get_links(spacex_url)
    
    for number, link in enumerate(links):
        filename = f'spaceX{number}.jpeg'
        get_image(link,filename)

def main():
    fetch_spacex_last_launch()

if __name__ == '__main__':
    main()
