valid_token = {
        'X-API-KEY': 'EXRZWW3-FN9MSY5-QRZEFC5-3EW7JCB'
    }

invalid_token = {
        'X-API-KEY': 'EXRZWW3-FN9MSY5-QRZEFC5-1111111'
    }

without_token = {
        'X-API-KEY': ''
    }


class UiTestData:
    def __init__(self, browser):
        self.browser = browser
    SEARCH_QUERY = 'Интерстеллар'
    LOCATOR_FIND_FILM = '//*[@id="find_film"]'
    FILM_YEAR = '2015'
    LOCATOR_FILM_YEAR = '//*[@id="year"]'
    ACTOR = 'Константин Хабенский'
    LOCATOR_ACTOR = '//*[@id="find_people"]'
    SERIAL = 'Метод'
    LOCATOR_ACTOR_MAIN_SEARCH = '//*[@id="formSearchMain"]/input[8]'
    STUDIO = 'Среда'
    LOCATOR_STUDIO = '//*[@id="find_studio"]'