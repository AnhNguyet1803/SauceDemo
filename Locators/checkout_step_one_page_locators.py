from selenium.webdriver.common.by import By


class CheckOutStepOnePageLocators(object):
    """A class for min page locators. All main page locators should come here"""
    INPUT_FIRSTNAME = (By.ID, 'first-name')
    INPUT_LASTNAME = (By.ID, 'last-name')
    INPUT_POSTALCODE = (By.ID, 'postal-code')
    BUTTON_CONTINUE = (By.XPATH, "//input[@class='btn_primary cart_button']")
    BUTTON_CANCEL = (By.XPATH, "//a[@class='cart_cancel_link btn_secondary']")
