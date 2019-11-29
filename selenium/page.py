from element import SearchTextElement
from locators import MainPageLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class IndexPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_correct(self):
        return "Booking.com | Официальный сайт" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
