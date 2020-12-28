from selenium.webdriver.common.by import By


class CartPageLocators(object):
    """A class for min page locators. All main page locators should come here"""
    BUTTON_CHECKOUT = (By.XPATH, "//div[@class='cart_footer']/a[text()='CHECKOUT']")
    BUTTON_CONTINUE = (By.XPATH, "//div[@class='cart_footer']/a[text()='Continue Shopping']")
    CART_ITEM = "//div[@class='cart_list']//div[@class='cart_item']["

    def BUTTON_REMOVE(index):
        ITEM = "]//button[text()='REMOVE']"
        return By.XPATH, (CartPageLocators.CART_ITEM + str(index) + ITEM)

    def LABEL_PRODUCT_QUANTITY(index):
        ITEM = "]//div[@class='cart_quantity']"
        return By.XPATH, (CartPageLocators.CART_ITEM + str(index) + ITEM)

    def LABEL_PRODUCT_NAME(index):
        ITEM = "]//div[@class='inventory_item_name']"
        return By.XPATH, (CartPageLocators.CART_ITEM + str(index) + ITEM)

    def LABEL_PRODUCT_DESC(index):
        ITEM = "]//div[@class='inventory_item_desc']"
        return By.XPATH, (CartPageLocators.CART_ITEM + str(index) + ITEM)

    def LABEL_PRODUCT_PRICE(index):
        ITEM = "]//div[@class='inventory_item_price']"
        return By.XPATH, (CartPageLocators.CART_ITEM + str(index) + ITEM)
