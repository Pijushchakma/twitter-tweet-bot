import requests
import os
import dotenv
from typing import List
import random
import constants

dotenv.load_dotenv()


ACCESS_KEY = os.environ['ACCESS_KEY']


def search_image()->List:
    query = random.choice(constants.TAGS)
    url = f'https://api.unsplash.com/search/photos?page=1&query={query}&client_id={ACCESS_KEY}'
    resp = requests.get(url)
    data = resp.json()['results']
    return data

def get_random_image():
    response_data = search_image()
    random_image_data = random.choice(response_data)
    link = random_image_data['urls']['full']
    return link


def download_image():
    filename = 'picture.jpg'
    image_url = get_random_image()
    image_response = requests.get(image_url,stream=True)
    if image_response.status_code == 200:
        with open(filename,'wb') as image_file:
            for chunk in image_response:
                image_file.write(chunk)






download_image()