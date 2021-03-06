import logging

from Locators.products_locators import ProductsPageLocators
from Objects.product import Product
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

    def get_product_info(self, index):
        name = self.get_text(ProductsPageLocators.LABEL_PRODUCT_NAME(index))
        desc = self.get_text(ProductsPageLocators.LABEL_PRODUCT_DESC(index))
        price = self.get_text(ProductsPageLocators.LABEL_PRODUCT_PRICE(index))

        product = Product(name, desc, price)
        print(product)
        return product

    def get_all_products_info(self):
        products = []
        for index in range(6):
            products.append(self.get_product_info(index + 1))

        return products

    def add_product_to_card(self, index):
        self.click(ProductsPageLocators.BUTTON_ADD_TO_CART(index))

    def does_add_button_exist(self, index):
        return self.is_visible(ProductsPageLocators.BUTTON_ADD_TO_CART(index))

    def remove_product_from_card(self, index):
        self.click(ProductsPageLocators.BUTTON_REMOVE(index))

    def does_remove_button_exist(self, index):
        return self.is_visible(ProductsPageLocators.BUTTON_REMOVE(index))

    def get_product_badge(self):
        total = 0
        try:
            total = self.get_text(ProductsPageLocators.ICON_BADGE_HAS_ITEMS)
        except:
            pass
        return int(total)

    def is_product_badge_invisible(self):
        return self.is_invisible(ProductsPageLocators.ICON_BADGE_HAS_ITEMS)
