import sys

from Utils.assertions import Assertion

sys.path.append(".")

import unittest

from Pages.login_page import LoginPage
from Pages.cart_pages import CartPage
from Pages.products_page import ProductsPage
from Testcases.base_test import BaseTest
from Testdata.data import Data
from Objects.account import Account
from Objects.check_out_step_one import CheckOutStepOne
from Pages.check_out_step_one_pages import CheckOutStepOnePages
from Pages.check_out_step_two_pages import CheckOutStepTwoPages
from Utils.utility import Utility


class TestCartProduct(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_checkout_products(self):
        assertion = Assertion()
        login_page = LoginPage(self.driver)
        account = Account('standard_user', Data.PASSWORD)
        login_page.login(account)

        products = Data.get_products_json(self)
        products_page = ProductsPage(self.driver)

        for index in [1, 2, 3]:
            products_page.click_add_to_cart_button(index)

        products_page.click_badge_icon()
        cart_page = CartPage(self.driver)

        for index in [1, 2, 3]:
            actual_product = cart_page.get_product_info(index)
            expected_product = products[index - 1]
            assertion.compare_products(actual_product, expected_product)

        cart_page.click_checkout()

        check_out_step_one_page = CheckOutStepOnePages(self.driver)
        check_out_step_one = CheckOutStepOne(Data.FIRSTNAME, Data.LASTNAME, Data.POSTALCODE)
        # check_out_step_one = CheckOutStepOne('a', 'b', '123')
        check_out_step_one_page.check_out_info(check_out_step_one)
        check_out_step_one_page.click_continue()

        check_out_step_two_page = CheckOutStepTwoPages(self.driver)
        total_price = 0.00
        for index in [1, 2, 3]:
            actual_product = check_out_step_two_page.get_product_info(index)
            expected_product = products[index - 1]
            assertion.compare_products(actual_product, expected_product)
            total_price += Utility().multiple(actual_product.quantity, actual_product.price)

        self.assertEqual(total_price, check_out_step_two_page.get_item_total())

        actual_tax = total_price * 0.08004
        self.assertEqual(float("{:.2f}".format(actual_tax)), check_out_step_two_page.get_tax())

        actual_total = total_price + actual_tax
        self.assertEqual(float("{:.2f}".format(actual_total)), check_out_step_two_page.get_total())
        print(actual_total)

        check_out_step_two_page.click_finish()


if __name__ == "__main__":
    unittest.main()
