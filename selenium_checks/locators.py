from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    HEADER_BUTTON_BLOCK = (By.CLASS_NAME, 'cross-product-bar__wrapper')
    ACCOMMODATION_BUTTON = (
        By.XPATH,
        "//*[contains(text(), 'Accommodations')]"
    )
    LANGUAGE_CHOICE_BUTTON = (
        By.XPATH,
        "//li[contains(@data-id, 'language_selector')]"
    )
    language_selector_template = (
        By.XPATH,
        "//span[contains(@lang, '{language_code}')]"
    )


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
