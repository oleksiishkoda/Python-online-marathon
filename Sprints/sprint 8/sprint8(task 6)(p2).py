##import unittest
##from unittest.mock import patch
##
##def file_parser(file, *strings):
##    count = 0
##    data = open(file, 'r')
##    if len(strings) == 1:
##        for line in data:
##            if strings[0] in line:
##                count += 1
##        data.close()
##    if len(strings) == 2:
##        lines = data.readlines()
##        write_data = open(file, 'w')    
##        for line in lines:
##            if strings[0] in line:
##                write_data.write(line.replace(strings[0], strings[1]))
##                count += 1
##            else:
##                write_data.write(line)
##        write_data.close
##        data.close()
##        return f"Replace {count} strings"
##    data.close()
##    return f"Found {count} strings"
##class ParserTest(unittest.TestCase):
##    def setUp(self):
##        self.f = open('test_parser', 'r')
##        
##    def test_is_equal(self):
##        for line in self.f:
##            with self.subTest():
##                
##
##
##    
##    def tearDown(self):
##        f.close()
##    



import unittest
from parameterized import parameterized    
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
                    self.a = item[0]
                    self.b = item[1]
                    self.c = item[2]
            else: 
                raise TriangleNotValidArgumentException("Not valid arguments")
                 
    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))





if __name__ == "__main__":
    # unittest.main()

    valid_test_data = [
    (3, 4, 5),
    (26, 25, 3),
    (30, 29, 5),
    (87, 55, 34),
    (120, 109, 13),
    (123, 122, 5)
    ]
    for data in valid_test_data:
        try:
            Triangle(data)
        except TriangleNotExistException as e:
            print(e)








