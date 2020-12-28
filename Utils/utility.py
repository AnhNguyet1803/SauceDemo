import json
import os
import re


class Utility:

    def get_browser(self):
        try:
            return os.environ['BROWSER']
        except:
            return 'chrome'

    def read_json(file_name):
        with open(file_name, 'r') as jsonfile:
            reader = json.load(jsonfile)
            jsonfile.close()
        return reader

    def convert_string_to_float(self, str):
        try:
            return float(re.findall("\d+\.\d+", str)[0])
        except:
            return 0.00

    def multiple(self, quantity, price):
        temp_price = self.convert_string_to_float(price)
        return int(quantity) * temp_price
