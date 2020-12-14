from selenium.webdriver.common.by import By


class ProductsPageLocators(object):
    """A class for min page locators. All main page locators should come here"""
    IMG_BROKEN = (By.XPATH, "//img[@class='inventory_item_img' and contains(@src, 'WithGarbageOnItToBreakTheUrl')]")
    PRO_NAME = (By.XPATH, "//img[@class='inventory_item_name' and contains(@text, 'Sauce Labs Backpack')]")
