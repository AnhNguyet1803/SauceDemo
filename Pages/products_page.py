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

    def get_badge_total(self):
        index = 0
        try:
            text = self.get_text(ProductsPageLocators.ICON_BADGE_HAS_ITEMS)
            index = int(text)
        except:
            return 0
        return index

    def click_badge_icon(self):
        self.click(ProductsPageLocators.ICON_BADGE_NO_ITEM)

    def click_remove_button(self, index):
        self.click(ProductsPageLocators.BUTTON_REMOVE(index))

    def click_add_to_cart_button(self, index):
        self.click(ProductsPageLocators.BUTTON_ADD_TO_CART(index))
