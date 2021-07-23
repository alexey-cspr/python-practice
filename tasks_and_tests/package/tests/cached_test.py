import unittest
from package import cached
from timeit import default_timer as timer

class CachedTest(unittest.TestCase):
    def setUp(self):
        def multi(a, b):
            return a * b
        self.multi = cached.cached(multi)

    def test_cached(self):
        start = timer()
        self.multi(int(123123),int(123123))
        point1 = timer() - start
        start = timer()
        self.multi(int(123123),int(123123))
        point2 = timer() - start
        self.assertTrue((point1/point2) == 1) 