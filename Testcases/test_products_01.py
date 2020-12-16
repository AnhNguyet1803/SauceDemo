import sys

sys.path.append(".")

import unittest
# import time

from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from Testcases.base_test import BaseTest
from Testdata.data import Data
from Objects.account import Account


class TestProduct(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_product(self):
        login_page = LoginPage(self.driver)
        account = Account('standard_user', Data.PASSWORD)
        login_page.login(account)

        products_page = ProductsPage(self.driver)
        # total = products_page.get_badge_total()
        # print(total)
        # products_page.click_badge_icon()
        products_page.click_add_to_cart_button(1)
        products_page.click_remove_button(1)


if __name__ == "__main__":
    unittest.main()
