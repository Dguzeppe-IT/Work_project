from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def enter_search_query(self, xpath, query):
        search_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        search_input.send_keys(query)
        search_input.submit()

    def enter_search_query_no_submit(self, xpath, query):
        search_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        search_input.send_keys(query)