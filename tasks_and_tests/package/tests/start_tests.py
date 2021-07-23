import unittest
from package.tests import cached_test
from package.tests import vector_test
from package.tests import sort_test
from package.tests import singleton_test
from package.tests import converter_test

def start():
    suite_cached = unittest.TestLoader().loadTestsFromModule(cached_test)
    suite_sort = unittest.TestLoader().loadTestsFromModule(sort_test)
    suite_json = unittest.TestLoader().loadTestsFromModule(converter_test)
    suite_singleton = unittest.TestLoader().loadTestsFromModule(singleton_test)
    suite_vector = unittest.TestLoader().loadTestsFromModule(vector_test)
    all_tests = unittest.TestSuite([suite_cached, suite_sort, suite_json, suite_singleton, suite_vector])
    unittest.TextTestRunner(verbosity=2).run(all_tests)