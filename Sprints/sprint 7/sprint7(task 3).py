class MotorCycle: 
    def __init__(self): 
        self.name = "MotorCycle"
    def TwoWheeler(self): 
        return "TwoWheeler"
class Truck: 
    def __init__(self): 
        self.name = "Truck"
    def EightWheeler(self): 
        return "EightWheeler"
class Car: 
    def __init__(self): 
        self.name = "Car"
    def FourWheeler(self): 
        return "FourWheeler"
class Adapter: 
    def __init__(self, obj, **adapted_methods): 
        self.obj = obj
        self.__dict__.update(adapted_methods)
    def __getattr__(self, attr): 
        return getattr(self.obj, attr)
    def original_dict(self): 
        return self.obj.__dict__
        
  
