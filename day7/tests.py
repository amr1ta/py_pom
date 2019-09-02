import unittest
import HtmlTestRunner
from pathlib import Path
from tests.test_search_page import TestSearchPage

test_suite = unittest.TestSuite()
tests = unittest.makeSuite(TestSearchPage)
test_suite.addTest(tests)

base_path = Path(__file__).parent
reportDir = (base_path / 'reports').resolve()
test_runner = HtmlTestRunner.HTMLTestRunner(output=reportDir)
test_runner.run(test_suite)
