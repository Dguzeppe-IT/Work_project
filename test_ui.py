import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import UI_CONFIG
from data import UI_TEST_DATA
import time


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_movie(browser):
    browser.get(UI_CONFIG['kino_search'])
    search_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="find_film"]'))
    )
    search_input.send_keys(UI_TEST_DATA['search_query'])
    search_input.submit()
    time.sleep(5)
    assert UI_TEST_DATA['search_query'] in browser.page_source


def test_search_movie_to_year(browser):
    browser.get(UI_CONFIG['kino_search'])
    search_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="year"]'))
    )
    search_input.send_keys(UI_TEST_DATA['film_year'])
    search_input.submit()
    time.sleep(5)
    assert UI_TEST_DATA['film_year'] in browser.page_source


def test_search_movie_to_actor(browser):
    browser.get(UI_CONFIG['kino_search'])
    search_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="find_people"]'))
    )
    search_input.send_keys(UI_TEST_DATA['actor'])
    search_input.submit()
    time.sleep(5)
    assert UI_TEST_DATA['actor'] in browser.page_source


def test_search_movie_to_studios(browser):
    browser.get(UI_CONFIG['kino_search'])
    search_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="find_studio"]'))
    )
    search_input.send_keys(UI_TEST_DATA['studio'])
    search_input.submit()
    time.sleep(5)
    assert UI_TEST_DATA['studio'] in browser.page_source


def test_search_movie_to_multiple_requests(browser):
    browser.get(UI_CONFIG['kino_search'])
    search_film = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="find_film"]'))
    )
    search_film.send_keys(UI_TEST_DATA['serial'])

    search_year = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="year"]'))
    )
    search_year.send_keys(UI_TEST_DATA['film_year'])

    search_actor = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="formSearchMain"]/input[8]'))
    )
    search_actor.send_keys(UI_TEST_DATA['actor'])
    search_actor.submit()
    time.sleep(5)

    assert UI_TEST_DATA['actor'] in browser.page_source
    assert UI_TEST_DATA['film_year'] in browser.page_source
    assert UI_TEST_DATA['serial'] in browser.page_source
