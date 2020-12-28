import logging

from Locators.checkout_step_one_page_locators import CheckOutStepOnePageLocators
from Pages.base_page import BasePage


class CheckOutStepOnePages(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def check_out_info(self, CheckOutStepOne):
        self.enter_text(CheckOutStepOnePageLocators.INPUT_FIRSTNAME, CheckOutStepOne.firstname)
        self.enter_text(CheckOutStepOnePageLocators.INPUT_LASTNAME, CheckOutStepOne.lastname)
        self.enter_text(CheckOutStepOnePageLocators.INPUT_POSTALCODE, CheckOutStepOne.postalcode)

    def click_continue(self):
        self.click(CheckOutStepOnePageLocators.BUTTON_CONTINUE)

    def click_cancel(self):
        self.click(CheckOutStepOnePageLocators.BUTTON_CANCEL)
