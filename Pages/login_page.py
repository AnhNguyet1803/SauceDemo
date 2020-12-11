import logging

from Locators.login_page_locators import LoginPageLocators
from Pages.base_page import BasePage
from Testdata.data import Data


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        self.navigate_to(Data.BASE_URL)

    def login(self, account):
        self.enter_text(LoginPageLocators.INPUT_USERNAME, account.username)
        self.enter_text(LoginPageLocators.INPUT_PASSWORD, account.password)
        self.click(LoginPageLocators.BUTTON_LOGIN)
