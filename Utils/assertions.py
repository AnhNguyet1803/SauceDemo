import logging
import unittest


class Assertion(unittest.TestCase):
    def compare_products(self, actual_product, expected_product):
        message = "Actual: '{}', Expect: '{}'"
        try:
            self.assertEqual(actual_product.name, expected_product.name)
        except AssertionError:
            logging.error(message.format(actual_product.name, expected_product.name))

        try:
            self.assertEqual(actual_product.desc, expected_product.desc)
        except AssertionError:
            logging.error(message.format(actual_product.desc, expected_product.desc))

        try:
            self.assertEqual(actual_product.price, expected_product.price)
        except AssertionError:
            logging.error(message.format(actual_product.price, expected_product.price))
        pass
