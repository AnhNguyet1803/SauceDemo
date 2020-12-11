import os
import sys

sys.path.append(".")

from Utils.HTMLTestRunner import *
from Testcases.test_login import SauceDemo

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Login class
test1 = unittest.TestLoader().loadTestsFromTestCase(SauceDemo)

# create a test suite
test_suite = unittest.TestSuite([test1])

# open the report file
outfile = open(dir + "/Reports/SeleniumPythonTestSummary.html", "w", encoding='utf-8')

# configure HTMLTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
outfile.close()
