import unittest
def divide(num_1, num_2):
    return float(num_1)/num_2

class DivideTest(unittest.TestCase):
    def test_one(self):
        excepted = 10
        actual = divide(100, 10)
        self.assertEqual(actual, excepted)
    def test_two(self):
        self.assertRaises(ZeroDivisionError, divide, 100, 0)
    def test_three(self):
        excepted = 3.33333333
        actual = divide(10, 3)
        self.assertAlmostEqual(actual, excepted, 7)

if __name__ == "__main__":
    unittest.main()