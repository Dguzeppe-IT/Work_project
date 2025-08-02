import requests
from config import API_CONFIG
from data import valid_token
from data import invalid_token

BASE_URL = API_CONFIG['base_url']


def test_search_movie_by_name_сyrillic():
    response = requests.get(
        f"{BASE_URL}/movie/",
        params={'query': 'Интерстеллар'},
        headers=valid_token
    )
    assert response.status_code == 200


def test_search_movie_by_name_latin():
    response = requests.get(
        f"{BASE_URL}/movie/",
        params={'query': 'Interstellar'},
        headers=valid_token
    )
    assert response.status_code == 200


def test_search_without_token():
    response = requests.get(
        f"{BASE_URL}/movie/",
        params={'query': 'Интерстеллар'},
    )
    assert response.status_code == 401


def test_search_with_invalid_token():
    response = requests.get(
        f"{BASE_URL}/movie/",
        params={'query': 'Интерстеллар'},
        headers=invalid_token
    )
    assert response.status_code == 500


def test_search_with_put_method():
    response = requests.put(
        f"{BASE_URL}/movie/",
        params={'query': 'Интерстеллар'},
        headers=valid_token
    )
    assert response.status_code == 404
