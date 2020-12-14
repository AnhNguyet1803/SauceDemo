import sys

sys.path.append(".")

import unittest

from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from Testdata.data import Data
from Objects.account import Account
from Pages.products_page import ProductsPage


class SauceDemo(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    @unittest.skip
    def test_login_standard_user(self):
        login_page = LoginPage(self.driver)
        account = Account('standard_user', Data.PASSWORD)
        login_page.login(account)

        products_page = ProductsPage(self.driver)
        url = products_page.get_product_url()

        # self.assertIn(url, 'https://www.saucedemo.com/inventory.html')
        self.assertIn('inventory.html', url)
        print(url)

    @unittest.skip
    def test_login_locked_out_user(self):
        login_page = LoginPage(self.driver)
        account = Account('locked_out_user', Data.PASSWORD)
        login_page.login(account)
        error_msg = login_page.get_error_message()

        self.assertIn('Sorry, this user has been locked out.', error_msg)

    def test_login_problem_user(self):
        login_page = LoginPage(self.driver)
        account = Account('problem_user', Data.PASSWORD)
        login_page.login(account)
        products_page = ProductsPage(self.driver)
        total = products_page.count_broken_images()
        self.assertEqual(0, total)

    @unittest.skip
    def test_login_performance_glitch_user(self):
        login_page = LoginPage(self.driver)
        account = Account('performance_glitch_user', Data.PASSWORD)
        login_page.login(account)

    @unittest.skip
    def test_login_standard(self):
        login_page = LoginPage(self.driver)
        account = Account('standard_user', 'secret_sauce!')
        login_page.login(account)

        error_msg = login_page.get_error_message()
        print(error_msg)
        self.assertIn('Username and password do not match any user in this service', error_msg)

    @unittest.skip
    def test_login_user(self):
        login_page = LoginPage(self.driver)
        account = Account('user', 'secret')
        login_page.login(account)


if __name__ == "__main__":
    unittest.main()
