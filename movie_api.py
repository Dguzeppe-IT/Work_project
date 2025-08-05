import requests
from config import API_CONFIG

BASE_URL = API_CONFIG['base_url']


class MovieAPI:
    def __init__(self, headers=None):
        self.base_url = BASE_URL
        self.headers = headers

    def search_movie_get(self, query):
        response = requests.get(
                f"{self.base_url}/movie/",
                params={'query': query},
                headers=self.headers)
        return response

    def search_movie_put(self, query):
        response = requests.put(
                f"{self.base_url}/movie/",
                params={'query': query},
                headers=self.headers)
        return response
