import json
import sys

from Objects.product import Product

sys.path.append(".")


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
        with open(Data.PRODUCT_JSON_FILE) as json_file:
            data = json.load(json_file)
            for obj in data['products']:
                product = Product(obj['name'], obj['desc'], obj['price'])
                products.append(product)
            json_file.close()
        return products

    # def read_products_from_json(self):
    #     products = []
    #
    #     with open(Data.PRODUCT_JSON_FILE) as jsonfile:
    #         reader = json.load(jsonfile)
    #         for row in reader['products']:
    #             products.append(row)
    #             print(row)
    #     jsonfile.close()
    #
    #     return products
