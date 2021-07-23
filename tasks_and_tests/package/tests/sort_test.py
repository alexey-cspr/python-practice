import unittest
from package import external_sort
import random

class SortTest(unittest.TestCase):
    def setUp(self):
        with open("data_input_file.txt", "w") as f:
            f.writelines('{}\n'.format(random.randint(-10000, 10000)) for i in range(10000))

    def test_sort(self):
        with open("data_input_file.txt", "r") as f:
            temp = f.readlines()
            temp = list(map(int, temp))
            temp.sort()
        external_sort.ex_sort("data_input_file.txt", "data_output_file.txt", 10000)
        with open("data_output_file.txt", "r") as f:
            result = f.readlines()
            result = list(map(int, result))
        self.assertEqual(result, temp)
        external_sort.ex_sort("data_input_file.txt", "data_output_file.txt", 1000)
        with open("data_output_file.txt", "r") as f:
            result = f.readlines()
            result = list(map(int, result))
        self.assertEqual(result, temp)