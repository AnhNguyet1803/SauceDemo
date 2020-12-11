import sys

sys.path.append(".")

import unittest

from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from Testdata.data import Data
from Objects.account import Account


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

    def test_login_locked_out_user(self):
        login_page = LoginPage(self.driver)
        account = Account('locked_out_user', Data.PASSWORD)
        login_page.login(account)

    def test_login_problem_user(self):
        login_page = LoginPage(self.driver)
        account = Account('problem_user', Data.PASSWORD)
        login_page.login(account)

    def test_login_performance_glitch_user(self):
        login_page = LoginPage(self.driver)
        account = Account('performance_glitch_user', Data.PASSWORD)
        login_page.login(account)

    def test_login_standard(self):
        login_page = LoginPage(self.driver)
        account = Account('standard_user', 'secret_sauce!')
        login_page.login(account)

    def test_login_user(self):
        login_page = LoginPage(self.driver)
        account = Account('user', 'secret')
        login_page.loginin(account)


if __name__ == "__main__":
    unittest.main()
