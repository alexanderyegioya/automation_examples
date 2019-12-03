import unittest
from selenium import webdriver
from selenium_checks import page


class BookingIndexPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.booking.com/")
        self.main_page = page.IndexPage(self.driver)

    def test_title(self):
        assert self.main_page.is_title_correct(), "booking.com title doesn't match."

    def test_header(self):
        # header button block
        self.main_page.is_header_buttons_visible()
        assert self.main_page.get_accommodation_button_text() == 'Проживание', 'text is not valid'

    # def test_search_ticket(self):
    #     # search tickets
    #     self.main_page.search_text_element = "pycon"
    #     self.main_page.click_go_button()
    #     search_results_page = page.SearchResultsPage(self.driver)
    #     # Verifies that the results page is not empty
    #     assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
