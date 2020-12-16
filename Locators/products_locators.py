from selenium.webdriver.common.by import By


class ProductsPageLocators(object):
    """A class for min page locators. All main page locators should come here"""
    IMG_BROKEN = (By.XPATH, "//img[@class='inventory_item_img' and contains(@src, 'WithGarbageOnItToBreakTheUrl')]")
    PRICE_ITEMS = (By.XPATH, "//div[@class='inventory_item_price']")
    ICON_BADGE_NO_ITEM = (By.XPATH, "//div[@class='shopping_cart_container']/a")
    ICON_BADGE_HAS_ITEMS = (By.XPATH, "//div[@class='shopping_cart_container']/a/span")

    PART1 = "//div[@class='inventory_item']["

    def BUTTON_REMOVE(self, index=1):
        part2 = "]//button[text()='REMOVE']"
        return By.XPATH, ProductsPageLocators.PART1 + str(index) + part2

    def BUTTON_ADD_TO_CART(self, index=1):
        part2 = "]//button[text()='ADD TO CART']"
        return By.XPATH, ProductsPageLocators.PART1 + str(index) + part2

    def LABEL_PRODUCT_NAME(self, index=1):
        part2 = "]//div[@class='inventory_item_name']"
        return By.XPATH, ProductsPageLocators.PART1 + str(index) + part2

    def LABEL_PRODUCT_DESC(self, index=1):
        part2 = "]//div[@class='inventory_item_desc']"
        return By.XPATH, ProductsPageLocators.PART1 + str(index) + part2

    def LABEL_PRODUCT_PRICE(self, index=1):
        part2 = "]//div[@class='inventory_item_price']"
        return By.XPATH, ProductsPageLocators.PART1 + str(index) + part2
