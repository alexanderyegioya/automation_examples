from selenium_checks.element import (
    SearchTextElement,
    LOCALIZATION,
    LanguageSelector,
    wait_for_element
)
from selenium_checks.locators import MainPageLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class IndexPage(BasePage):
    search_text_element = SearchTextElement()

    def choose_language(self, lang):
        wait_for_element(
            self.driver,
            10,
            MainPageLocators.LANGUAGE_CHOICE_BUTTON
        )
        lang_choice_button = self.driver.find_element(
            *MainPageLocators.LANGUAGE_CHOICE_BUTTON
        )
        lang_choice_button.click()

        language_button_locator = LanguageSelector(
            lang
        ).get_xpath_locator()

        wait_for_element(
            self.driver,
            10,
            language_button_locator
        )

        language_button = self.driver.find_element(
            *language_button_locator
        )
        language_button.click()
        print('{} language chosen'.format(lang))

    def is_title_correct(self, lang):
        local_title = LOCALIZATION[lang]['title']
        return "Booking.com | {title}".format(
            title=local_title
        ) in self.driver.title

    def is_header_buttons_visible(self):
        elem = self.driver.find_element(
            *MainPageLocators.HEADER_BUTTON_BLOCK
        )
        return elem.is_displayed()

    def get_button_text(self, locator):
        elem = self.driver.find_element(
            locator
        )
        return elem.text

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
