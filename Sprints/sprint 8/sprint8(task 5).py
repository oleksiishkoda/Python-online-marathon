import unittest

class Worker:
    def __init__(self, name, salary = 0):
        self.name = name
        if salary < 0: raise ValueError
        else: self.salary = salary
    def get_tax_value(self):
        taxes = {
            1000: 0,
            3000: 0.1,
            5000: 0.15,
            10000: 0.21,
            20000: 0.3,
            50000: 0.4,
            'more': 0.47
        }
        result = float(0)
        temp = 0
        for key in taxes:
            if key != "more" and self.salary > (key-temp):
                result += (key-temp) * taxes[key]
                self.salary -= (key-temp)
                temp = key
            else: 
                result += self.salary * taxes[key]
                break
        return result

class WorkerTest(unittest.TestCase):
    first = [-10000, -230000, -344000]
    second = {1550.0: 10000, 101150.0: 230000, 154730.0: 344000}        #key it's taxes; value it's salary.
    def setUp(self):
        self.my_obj = Worker("Oleksii")
        self.my_obj.salary = {"key1": "value1", "key2": "value2"}

    @unittest.expectedFailure
    def test_negative_salary(self):
        for data in WorkerTest.first:
            self.my_obj.salary = data
            with self.subTest():
                with self.assertRaises(ValueError):
                    self.my_obj.salary < 0

    def test_valid(self):
        for key, value in WorkerTest.second.items():
            with self.subTest():
                self.assertEqual(key, Worker("Borys", value).get_tax_value())

    def tearDown(self):
        self.my_obj = None
if __name__ == "__main__":
    unittest.main()
    # worker = Worker("Vika", 10000)
    # print(worker.get_tax_value())