import json
import os


class Utility():

    def get_browser(self):
        try:
            return os.environ['BROWSER']
        except:
            return 'chrome'

    def read_json(self, fileName):
        data = []
        with open(fileName, 'r') as jsonfile:
            reader = json.load(jsonfile)
            for row in reader:
                data.append(row)
            return data
