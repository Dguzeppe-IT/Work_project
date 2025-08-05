import pytest
from selenium import webdriver
from config import UI_CONFIG
from search_page import SearchPage
from data import UiTestData


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("xpath, query", [
    (UiTestData.LOCATOR_FIND_FILM, UiTestData.SEARCH_QUERY),
    (UiTestData.LOCATOR_FILM_YEAR, UiTestData.FILM_YEAR),
    (UiTestData.LOCATOR_ACTOR, UiTestData.ACTOR),
    (UiTestData.LOCATOR_STUDIO, UiTestData.STUDIO),
])
def test_search(browser, xpath, query):
    search_page = SearchPage(browser)
    search_page.open(UI_CONFIG['kino_search'])
    search_page.enter_search_query(xpath, query)
    assert query in browser.page_source


def test_search_movie_to_multiple_requests(browser):
    search_page = SearchPage(browser)
    search_page.open(UI_CONFIG['kino_search'])

    search_page.enter_search_query_no_submit(UiTestData.LOCATOR_FIND_FILM,
                                             UiTestData.SERIAL)
    search_page.enter_search_query_no_submit(UiTestData.LOCATOR_FILM_YEAR,
                                             UiTestData.FILM_YEAR)
    search_page.enter_search_query(UiTestData.LOCATOR_ACTOR_MAIN_SEARCH,
                                   UiTestData.ACTOR)

    assert UiTestData.ACTOR in browser.page_source
    assert UiTestData.FILM_YEAR in browser.page_source
    assert UiTestData.SERIAL in browser.page_source
