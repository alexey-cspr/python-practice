from package import vector
import unittest

class VectorTest(unittest.TestCase):
    def setUp(self):
        self.vector1 = vector.Vector(1, 2, 3, 4, 5)
        self.vector2 = vector.Vector(1, 3, 5, 7, 9)
        self.vector3 = vector.Vector(1, 1, 1, 1, 1, 1)

    def test_init(self):
        with self.assertRaises(TypeError):
            vec = vector.Vector(1, 'f')
    
    def test_len(self):
        result = self.vector1.__len__()
        self.assertEqual(result, 5)
    
    def test_index(self):
        result = self.vector1.__getitem__(3)
        self.assertEqual(result, 3)
        # with self.assertRaises(vector.VectorError):
        #     self.vector1.__getitem__(6)
        
    def test_add(self):
        result = self.vector1 + self.vector2
        self.assertEqual(result, vector.Vector(2, 5, 8, 11, 14))
        with self.assertRaises(vector.VectorError):
            self.vector1 + self.vector3

    def test_sub(self):
        result = self.vector2 - self.vector1
        self.assertEqual(result, vector.Vector(0, 1, 2, 3, 5))
        # with self.assertRaises(vector.VectorError):
        #     self.vector1 - vector.Vector(0, 1, 2, 3, 5, 0, 1, 2, 3, 5)

    def test_eq(self):
        result = self.vector1 == self.vector1
        self.assertTrue(result)
        result = self.vector1 == self.vector2
        self.assertTrue(result)
        self.assertFalse(self.vector2, self.vector3)

    def test_mul(self):
        result = self.vector1 * self.vector2
        self.assertEqual(result, vector.Vector(1, 6, 15, 28, 45))
        with self.assertRaises(vector.VectorError):
            self.vector1 * self.vector3
        result = self.vector2 * 2
        self.assertEqual(result, vector.Vector(2, 6, 10, 14, 18))