import pytest
from movie_api import MovieAPI
from data import valid_token, invalid_token, without_token


@pytest.fixture
def movie_api():
    return MovieAPI()


@pytest.mark.parametrize("query, expected_status_code", [
    ("Интерстеллар", 200),
    ("Interstellar", 200),
])
def test_search_movie_by_name(movie_api, query, expected_status_code):
    movie_api.headers = valid_token
    response = movie_api.search_movie_get(query)
    assert response.status_code == expected_status_code


def test_search_without_token(movie_api):
    movie_api.headers = without_token
    response = movie_api.search_movie_get("Интерстеллар")
    assert response.status_code == 401


def test_search_with_invalid_token(movie_api):
    movie_api.headers = invalid_token
    response = movie_api.search_movie_get("Интерстеллар")
    assert response.status_code == 500


def test_search_with_put_method(movie_api):
    movie_api.headers = valid_token
    response = movie_api.search_movie_put("Интерстеллар")
    assert response.status_code == 404
