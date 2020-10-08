# type your code here
def logger(func):
    def inner(*b, **keyword):
        x = func(*b, **keyword)
        lst = []
        for item in b:
            lst.append(str(item))
        for key in keyword:
            lst.append(str(keyword[key]))
        res = ", ".join(lst)
        print("Executing of function %s with arguments %s..."%(func.__name__, res))
        return x
    return inner
    
@logger
def concat(*b, **keyword):
    lst = []
    for item in b:
        lst.append(str(item))
    for key in keyword:
        lst.append(str(keyword[key]))
    res = "".join(lst)
    return res
    
@logger
def sum(a, b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)
    

a = print_arg(2)
print(a)
