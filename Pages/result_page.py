import logging

from Locators.result_page_locators import ResultPageLocators
from Pages.base_page import BasePage


class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def get_message(self):
        return self.get_text(ResultPageLocators.LABEL_MESSAGE)
