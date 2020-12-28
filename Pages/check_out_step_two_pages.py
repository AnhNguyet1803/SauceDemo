import logging

from Locators.checkout_step_two_page_locators import CheckoutTwoPageLocators
from Objects.product import Product
from Pages.base_page import BasePage
from Utils.utility import Utility


class CheckOutStepTwoPages(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def get_product_info(self, index):
        name = self.get_text(CheckoutTwoPageLocators.LABEL_PRODUCT_NAME(index))
        desc = self.get_text(CheckoutTwoPageLocators.LABEL_PRODUCT_DESC(index))
        price = self.get_text(CheckoutTwoPageLocators.LABEL_PRODUCT_PRICE(index))
        quantity = self.get_text(CheckoutTwoPageLocators.LABEL_PRODUCT_QUANTITY(index))
        product = Product(name, desc, price, quantity)
        return product

    def click_finish(self):
        self.click(CheckoutTwoPageLocators.BUTTON_FINISH)

    def click_cancel(self):
        self.click(CheckoutTwoPageLocators.BUTTON_CANCEL)

    def get_item_total(self, auto_convert=True):

        text = self.get_text(CheckoutTwoPageLocators.LABEL_ITEM_TOTAL)
        if auto_convert:
            return Utility().convert_string_to_float(text)
        else:
            return

    def get_tax(self, auto_convert=True):
        text = self.get_text(CheckoutTwoPageLocators.LABEL_TAX)
        if auto_convert:
            return Utility().convert_string_to_float(text)
        else:
            return

    def get_total(self, auto_convert=True):
        text = self.get_text(CheckoutTwoPageLocators.LABEL_TOTAL)
        if auto_convert:
            return Utility().convert_string_to_float(text)
        else:
            return
