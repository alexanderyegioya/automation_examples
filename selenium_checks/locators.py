from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    HEADER_BUTTON_BLOCK = (By.CLASS_NAME, 'cross-product-bar__wrapper')
    # ACCOMMODATION_BUTTON = (
    #     By.XPATH,
    #     "//*[contains(text(), 'Accommodations')]"
    # )
    ACCOMMODATION_BUTTON = (
        By.CSS_SELECTOR,
        'span.xpb__link'
    )
    FLIGHTS_BUTTON = (
        By.CSS_SELECTOR,
        'a.xpb__link:nth-child(2)'
    )
    CAR_RENTALS_BUTTON = (
        By.CSS_SELECTOR,
        'a.xpb__link:nth-child(3)'
    )
    TOURS_N_ACTIVITIES_BUTTON = (
        By.CSS_SELECTOR,
        'a.xpb__link:nth-child(4)'
    )
    AIRPORT_TAXIS_BUTTON = (
        By.CSS_SELECTOR,
        'a.xpb__link:nth-child(5)'
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
