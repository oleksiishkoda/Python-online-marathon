from abc import ABC, abstractmethod
class Product(ABC):
    @abstractmethod
    def cook(self):
        pass

class FettucineAlfredo(Product):
    def cook(self):
        self.name = "Fettuccine Alfredo"
        print(f"Italian main course prepared: {self.name}")
class Tiramisu(Product):
    def cook(self):
        self.name = "Tiramisu"
        print(f"Italian dessert prepared: {self.name}")
class DuckALOrange(Product):
    def cook(self):
        self.name = "Duck À L'Orange"
        print(f"French main course prepared: {self.name}")
class CremeBrulee(Product):
    def cook(self):
        self.name = "Crème brûlée"
        print(f"French dessert prepared: {self.name}")

class Factory(ABC):
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass
class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        self.type_of_meal = type_of_meal
        if self.type_of_meal == "main": return FettucineAlfredo()
        else: return Tiramisu()
class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        self.type_of_meal = type_of_meal
        if type_of_meal == "main": return DuckALOrange()
        else: return CremeBrulee()
class FactoryProducer():
    def get_factory(self, type_of_factory):
        self.type_of_factory = type_of_factory
        if self.type_of_factory == "italian": return ItalianDishesFactory()
        else: return FrenchDishesFactory()
