import unittest
from selenium import webdriver
import page


class BookingIndexPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.booking.com/")

    def test_header(self):

        main_page = page.MainPage(self.driver)
        # Checks if the word "Python" is in title
        assert main_page.is_title_correct(), "python.org title doesn't match."
        # Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
