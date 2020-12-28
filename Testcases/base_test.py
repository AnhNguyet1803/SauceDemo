import sys

sys.path.append(".")

import unittest

from selenium import webdriver
from Utils.utility import Utility


class BaseTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        # Setting up how we want Chrome to run
        utility = Utility()
        browser = utility.get_browser()
        self.driver = self.startBrowser(browser)
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            pass

    def startBrowser(name):

        try:
            if name.lower() == 'firefox' or name.lower() == 'ff':
                print('start browser name Firefox')
                return webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')
                # return webdriver.Firefox()
            elif name.lower() == 'chrome':
                print('start browser name Chrome')
                return webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
                # return webdriver.Chrome()
            elif name.lower() == 'phantomjs':
                print('start browser name PhantomJS')
                return webdriver.PhantomJS()
            else:
                print("Not found this browser, You can use 'firefox', 'chrome'")
                return webdriver.Firefox()
        except Exception as msg:
            print('message: %s' % str(msg))
