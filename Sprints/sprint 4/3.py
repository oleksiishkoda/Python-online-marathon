class Employee:
    def __init__(self, fullname, **kwargs):
        self.name = fullname.split(' ')[0]
        self.lastname = fullname.split(' ')[1]
        self.__dict__.update(kwargs)