import sys

sys.path.append(".")

from Utils.utility import Utility
from Objects.product import Product


class Data():
    BASE_URL = 'https://www.saucedemo.com/'
    USERNAME = 'standard_user'
    # USERNAME = 'locked_out_user'
    # USERNAME = 'problem_user'
    # USERNAME = 'performance_glitch_user'
    # USERNAME = 'user'
    PASSWORD = 'secret_sauce'
    # PASSWORD = 'secret_sauce!'
    BROWSER = 'Chrome'

    PRODUCT_JSON_FILE = './Testdata/products.json'

    def read_products_from_json(self):
        products = []
        utility = Utility()
        temp = utility.read_json(Data.PRODUCT_JSON_FILE)
        for obj in temp:
            product = Product(obj['name'], obj['desc'], obj['price'])
            products.append(product)
            print(product)
        return products
