class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    @classmethod
    def from_string(cls, x):
        lst = x.split('-')
        return cls(lst[0], lst[1], lst[2])
            
emp2 = Employee.from_string("John-Smith-15000")
print(type(emp2))
print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)