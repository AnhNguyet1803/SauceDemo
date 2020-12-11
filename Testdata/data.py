import sys

sys.path.append(".")

from Utils.utility import Utility


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

    ACCOUNT_CSV_FILE = './Testdata/accounts.csv'
    ACCOUNT_JSON_FILE = './Testdata/accounts.json'

    # def get_account_csv(self):
    #     utility = Utility()
    #     return utility.read_csv(Data.ACCOUNT_CSV_FILE)

    def get_account_json(self):
        utility = Utility()
        return utility.read_json(Data.ACCOUNT_JSON_FILE)
