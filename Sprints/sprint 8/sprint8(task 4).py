import unittest
from math import sqrt
class TriangleNotValidArgumentException(Exception):
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return self.data

class TriangleNotExistException(Exception):
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return self.data

class Triangle:
    def __init__(self, *lst):
        for args in lst:
            if isinstance(args, tuple) and len(args) == 3 and isinstance(args[0], int) \
            and isinstance(args[1], int) and isinstance(args[2], int):
                if (args[0] + args[1]) <= args[2] or (args[1] + args[2]) <= args[0] \
                or (args[0] + args[2]) <= args[1]:
                    raise TriangleNotExistException("Can`t create triangle with this arguments")
                else:
                    self.a = args[0]
                    self.b = args[1]
                    self.c = args[2]
            else: 
                raise TriangleNotValidArgumentException("Not valid arguments")
                 
    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))


class TriangleTest(unittest.TestCase):
    def setUp(self):
        self.valid_data = [((3, 4, 5), 6.0), ((10, 10, 10), 43.30), ((6, 7, 8), 20.33)]
        self.invalid_data = [("3", 4, 5), ("a", 2, 3), ("string")]
        self.invalid_triangle = [(1, 2, 3), (1, 1, 2), (7, 7, 15)]

    def test_exception(self):
        for item in self.invalid_data:
            with self.subTest():
                self.assertRaises(TriangleNotValidArgumentException, Triangle, item)

    def test_sides(self):
        for item in self.invalid_triangle:
            with self.subTest():
                self.assertRaises(TriangleNotExistException, Triangle, item)

    def test_area(self):
        for item in self.valid_data:
            self.assertEqual(item[1], round(Triangle(item[0]).get_area(), 2)) #заокрулюю до 2 знаків після коми

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()