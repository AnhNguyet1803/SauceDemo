from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for min page locators. All main page locators should come here"""
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.XPATH, "//*[@id='login-button']")
