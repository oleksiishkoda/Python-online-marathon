import unittest
class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

class Cart:
    def __init__(self, *products):
        self.cart = []
        for prod in products:
            self.cart.append(prod)
    def total_count_and_price(self):
        self.tot_count = 0
        self.tot_price = 0
        for product in self.cart:
            self.tot_count += product.count
            self.tot_price += product.price
        if self.tot_count <= 2: return self.tot_price
        elif self.tot_count <= 5: return self.tot_price - (self.tot_price * 0.05)
        elif self.tot_count <= 7: return self.tot_price - (self.tot_price * 0.1)
        elif self.tot_count <= 10: return self.tot_price - (self.tot_price * 0.2)
        elif self.tot_count <= 20: return self.tot_price - (self.tot_price * 0.3)
        else: return self.tot_price - (self.tot_price * 0.5)
        
class CartTest(unittest.TestCase):
    def test_cart(self):
        banana = Product("banana", 20, 2)
        apple = Product("apple", 25, 3)
        mango = Product("mango", 30, 4)
        a = Cart(banana, apple, mango)
        expected = 60
        actual = a.total_count_and_price()
        self.assertEqual(expected, actual)



if __name__ == "__main__":

    unittest.main()
