from selenium_checks.element import SearchTextElement
from selenium_checks.locators import MainPageLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class IndexPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_correct(self):
        return "Booking.com | Официальный сайт" in self.driver.title

    def is_header_buttons_visible(self):
        element = self.driver.find_element(
            *MainPageLocators.HEADER_BUTTON_BLOCK
        )
        return element.is_displayed()

    def get_accommodation_button_text(self):
        elem = self.driver.find_element(
            *MainPageLocators.ACCOMMODATION_BUTTON
        )
        return elem.text

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def choose_language(self, lang):
        pass


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
