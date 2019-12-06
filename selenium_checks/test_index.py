import unittest
import argparse
from selenium import webdriver
from selenium_checks import page
from selenium_checks.element import LOCALIZATION
from selenium_checks.locators import MainPageLocators


class BookingIndexPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.main_page = page.IndexPage(self.driver)

    def test_title(self):
        self.driver.get("https://www.booking.com/")
        self.main_page.choose_language('ru')
        assert self.main_page.is_title_correct('ru'), "booking.com title doesn't match."

    def test_header(self):
        # header button block
        self.main_page.is_header_buttons_visible()
        assert self.main_page.get_button_text(
            *MainPageLocators.ACCOMMODATION_BUTTON
        ) == 'Проживание', 'text is not valid'

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            'Choose localizations to test: '
            'provide list or use flag --all_localizations'
        )
    )
    parser.add_argument(
        '--localizations',
        type=str,
        help='Provide list of localizations. Example: "ru,en-us,..."'
    )
    parser.add_argument(
        '--all_localizations',
        action='store_true',
        help='Set it to check all localizations'
    )
    args = parser.parse_args()

    if not (
            args.localizations and args.all_localizations
    ) and (
            args.localizations or args.all_localizations
    ):
        localizations = args.localizations.split(',') if args.localizations else LOCALIZATION.keys()
        unittest.main()
    else:
        raise Exception(
            'Set one option: all_localizations or localizations'
        )
