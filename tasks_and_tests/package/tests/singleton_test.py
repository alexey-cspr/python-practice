import unittest
from package import singleton

class SingletonTest(unittest.TestCase):
    def setUp(self):
        class Test(metaclass = singleton.Singleton):
            pass
        self.singleton1 = Test()
        self.singleton2 = Test()

    def test_singleton_class(self):
        self.assertEqual(self.singleton1, self.singleton2)