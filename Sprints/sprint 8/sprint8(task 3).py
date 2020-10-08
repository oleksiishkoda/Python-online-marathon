# import unittest
# from math import sqrt
# def quadratic_equation(a, b, c):
#     if a == 0:
#         raise ValueError
#     else:
#         discriminant = b**2 - 4*a*c
#         if discriminant > 0:
#             x1 = (-b + sqrt(discriminant))/(2*a)
#             x2 = (-b - sqrt(discriminant))/(2*a)
#             return x1, x2
#         elif discriminant == 0: return -b/(2*a)
#         else: return None

# class QuadraticEquationTest(unittest.TestCase):
#     def test_positive(self):
#         a = 1; b = 4; c = -21                   # x**2+4*x-21=0
#         x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
#         x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
#         expected = x1, x2
#         actual = quadratic_equation(a, b, c)
#         self.assertEqual(expected, actual)
#     def test_zero(self):    
#         a = 0; b = 4; c = -21
#         self.assertRaises(ValueError, quadratic_equation, a, b, c)
#     def test_negative(self):
#         a = 1; b = 2; c = 3
#         self.assertIsNone(quadratic_equation(a, b, c))
#     def test_disc_zero(self):
#         a = 1; b = 2; c = 1
#         expected = -b/(2*a)
#         self.assertEqual(expected, quadratic_equation(a, b, c))
# if __name__ == "__main__":
    
#     unittest.main()

import unittest
import cmath

def quadratic_equation(a,b,c):
  d = (b ** 2) - (4 * a * c)  
  if a == 0:
    raise ValueError('error')

  if d < 0:
    return None 
  x1 = (-b - d**0.5) / (2 * a)
  x2 = (-b + d**0.5) / (2 * a)
  if d == 0:
    return x2
  return x2,x1


class QuadraticEquationTest(unittest.TestCase):
  
  def test_negative_discriminant(self):
    given = quadratic_equation(2, 1, -1)
    expected = (0.5, -1.0)
    self.assertEqual(given, expected)

  def test_positive_discriminant(self):
    given = quadratic_equation(1, -4, 4)
    expected = (2.0)
    self.assertEqual(given, expected)

  def test_zero_discriminant(self):
    self.assertRaises(ValueError, quadratic_equation, 0, 6, 3)


unittest