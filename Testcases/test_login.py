import sys

sys.path.append(".")

import unittest

from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from Testdata.data import Data
from Objects.account import Account
from Pages.result_page import ResultPage


class SauceDemo(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_login_standard_user(self):
        login_page = LoginPage(self.driver)
        account = Account('standard_user', Data.PASSWORD)
        login_page.login(account)

    # def test_login_locked_out_user(self):
    #     login_page = LoginPage(self.driver)
    #     account = Account('locked_out_user', Data.PASSWORD)
    #     login_page.login(account)
    #
    # def test_login_problem_user(self):
    #     login_page = LoginPage(self.driver)
    #     account = Account('problem_user', Data.PASSWORD)
    #     login_page.login(account)
    #
    # def test_login_performance_glitch_user(self):
    #     login_page = LoginPage(self.driver)
    #     account = Account('performance_glitch_user', Data.PASSWORD)
    #     login_page.login(account)
    #
    # def test_login_standard(self):
    #     login_page = LoginPage(self.driver)
    #     account = Account('standard_user', 'secret_sauce!')
    #     login_page.login(account)

    def test_login_user(self):
        data = Data()
        login_page = LoginPage(self.driver)
        account = Account('user', 'secret')
        login_page.login(account)

        # result_page = ResultPage(self.driver)

        # print(result_page.get_message())
        # self.assertIn("Epic sadface: Username and password do not match any user in this service", result_page.get_message())

        message = data.get_message_json()
        for msg in message:
            message = msg['message']
            result_page = ResultPage(self.driver)
            self.assertIn(message, result_page.get_message())
            print(result_page.get_message())


if __name__ == "__main__":
    unittest.main()
