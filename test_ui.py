import pytest
from selenium import webdriver
from config import UI_CONFIG
from data import UI_TEST_DATA
from search_page import SearchPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("xpath, query, expected_result", [
    ('//*[@id="find_film"]', UI_TEST_DATA['search_query'],
     UI_TEST_DATA['search_query'])
])
def test_search_movie(browser, xpath, query, expected_result):
    search_page = SearchPage(browser)
    search_page.open(UI_CONFIG['kino_search'])
    search_page.enter_search_query(xpath, query)
    assert expected_result in browser.page_source


@pytest.mark.parametrize("xpath, query, expected_result", [
    ('//*[@id="year"]', UI_TEST_DATA['film_year'], UI_TEST_DATA['film_year'])
])
def test_search_movie_to_year(browser, xpath, query, expected_result):
    search_page = SearchPage(browser)
    search_page.open(UI_CONFIG['kino_search'])
    search_page.enter_search_query(xpath, query)
    assert expected_result in browser.page_source


@pytest.mark.parametrize("xpath, query, expected_result", [
    ('//*[@id="find_people"]', UI_TEST_DATA['actor'], UI_TEST_DATA['actor'])
])
def test_search_movie_to_actor(browser, xpath, query, expected_result):
    search_page = SearchPage(browser)
    search_page.open(UI_CONFIG['kino_search'])
    search_page.enter_search_query(xpath, query)
    assert expected_result in browser.page_source


@pytest.mark.parametrize("xpath, query, expected_result", [
    ('//*[@id="find_studio"]', UI_TEST_DATA['studio'], UI_TEST_DATA['studio'])
])
def test_search_movie_to_studios(browser, xpath, query, expected_result):
    search_page = SearchPage(browser)
    search_page.open(UI_CONFIG['kino_search'])
    search_page.enter_search_query(xpath, query)
    assert expected_result in browser.page_source


def test_search_movie_to_multiple_requests(browser):
    search_page = SearchPage(browser)
    search_page.open(UI_CONFIG['kino_search'])

    search_page.enter_search_query_no_submit('//*[@id="find_film"]',
                                             UI_TEST_DATA['serial'])
    search_page.enter_search_query_no_submit('//*[@id="year"]',
                                             UI_TEST_DATA['film_year'])
    search_page.enter_search_query('//*[@id="formSearchMain"]/input[8]',
                                   UI_TEST_DATA['actor'])

    assert UI_TEST_DATA['actor'] in browser.page_source
    assert UI_TEST_DATA['film_year'] in browser.page_source
    assert UI_TEST_DATA['serial'] in browser.page_source
