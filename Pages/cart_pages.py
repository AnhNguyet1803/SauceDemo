from Locators.cart_page_locators import CartPageLocators
from Objects.product import Product
from Pages.base_page import BasePage


class CartPage(BasePage):
    def get_product_info(self, index):
        name = self.get_text(CartPageLocators.LABEL_PRODUCT_NAME(index))
        desc = self.get_text(CartPageLocators.LABEL_PRODUCT_DESC(index))
        price = self.get_text(CartPageLocators.LABEL_PRODUCT_PRICE(index))
        quantity = self.get_text(CartPageLocators.LABEL_PRODUCT_QUANTITY(index))

        return Product(name, desc, price, quantity)

    def click_checkout(self):
        self.click(CartPageLocators.BUTTON_CHECKOUT)

    def click_continue(self):
        self.click(CartPageLocators.BUTTON_CONTINUE)
