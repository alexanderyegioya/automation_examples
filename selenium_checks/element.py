from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium_checks.locators import MainPageLocators as mp_loc

LOCALIZATION = {
    'ru': {
        'title': 'Официальный сайт',
        'index_page': {
            'accommodations_button': 'Проживание',
            'flights_button': 'Авиабилеты',
            'car_rentals_button': 'Аренда машин',
            'tours_n_activities_button': 'Экскурсии и развлечения',
            'airport_taxis_button': 'Такси от/до аэропорта'
        }
    },
    'en-us': {
        'title': 'Official site',
        'index_page': {
            'accommodations_button': 'Accommodations',
            'flights_button': 'Flights',
            'car_rentals_button': 'Car Rentals',
            'tours_n_activities_button': 'Tours & Activities',
            'airport_taxis_button': 'Airport Taxis'
        }
    }
}


def wait_for_element(driver, timeout, locator):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            locator
        )
    )


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 'q'


class LanguageSelector():
    def __init__(self, lang):
        self.lang = lang

    def get_xpath_locator(self):
        return (
            mp_loc.language_selector_template[0],
            mp_loc.language_selector_template[1].format(
                language_code=self.lang
            )
        )
