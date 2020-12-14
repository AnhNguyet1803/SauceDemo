import logging

from Locators.products_locators import ProductsPageLocators
from Pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def get_product_url(self):
        return self.get_current_url()

    def count_broken_images(self):
        return self.get_elements_size(ProductsPageLocators.IMG_BROKEN)
