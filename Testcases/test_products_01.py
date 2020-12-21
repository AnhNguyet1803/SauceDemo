import sys

sys.path.append(".")

import unittest
# import time

from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from Testcases.base_test import BaseTest
from Testdata.data import Data
from Objects.account import Account
from Utils.assertions import Assertion


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
        # products_page.click_add_to_cart_button(1)
        # products_page.click_remove_button(1)

        # products_page.get_all_products_info()
        products = Data.read_products_from_json(self)

        for index, expected_product in enumerate(products, start=1):
            '''Add & remove all products'''
            products_page.add_product_to_card(index)
            self.assertTrue(products_page.does_remove_button_exist(index))

            products_page.remove_product_from_card(index)
            self.assertTrue(products_page.does_add_button_exist(index))

            actual_product = products_page.get_product_info(index)
            assertion = Assertion()
            assertion.compare_products(actual_product, expected_product)


if __name__ == "__main__":
    unittest.main()
