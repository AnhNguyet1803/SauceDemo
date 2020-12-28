import sys

from Objects.product import Product
from Utils.utility import Utility

sys.path.append(".")


class Data:
    BASE_URL = 'https://www.saucedemo.com/'
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    BROWSER = 'Chrome'
    FIRSTNAME = 'Standard'
    LASTNAME = 'User'
    POSTALCODE = '123456'

    PRODUCTS_JSON_FILE = 'Testdata/products.json'

    def get_products_json(self):
        products = []
        data = Utility.read_json(Data.PRODUCTS_JSON_FILE)
        for item in data['products']:
            product = Product(item['name'], item['desc'], item['price'])
            products.append(product)
        return products
