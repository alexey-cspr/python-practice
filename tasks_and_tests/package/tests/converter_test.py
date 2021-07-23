import unittest
from package import json_converter
import json

class ConverterTest(unittest.TestCase):
    def setUp(self):
        self.python_data = {
            'model': "mazda",
            "year": 2017,
            "mileage": 10000.923,
            "tires": ("winter", "summer"),
            "work": True,
            "not work": False,
            "driver": None,
            "brothers": [
                {"model": "bmw", "year": 2020},
                {"model": "chevrolet", "year": 2013}
            ]
        }
        self.json_data = '{"model": "mazda", "year": 2017, "mileage": 10000.923, "tires": ["winter", "summer"], '\
            '"work": true , "not work": false, "driver": null, "brothers":[{"model": "bmw", "year": 2020}, {"model": "chevrolet", "year": 2013}]}'

    def test_python_to_json(self):
        result = json_converter.python_to_json(self.python_data)
        self.assertEqual(result, json.dumps(self.python_data))

    def test_json_to_python(self):
        result = json_converter.json_to_python(self.json_data)
        self.assertEqual(result, json.loads(self.json_data))