##def func(item, lst=[]):
##    lst.append(item)
##    print(lst, end = " ")
##
##print(func(1))
##print(func(2))
##def f():
##    mes = "Outer string variable"
##    def inner():
##        nonlocal mes
##        mes = "Inner string variable"
##    inner()
##    return mes
##print(f())
##def f(a):
##    a = [1, 2]
##    print(a, end = " ")
##
##a = [1, 3]
##f(a)
##print(a)

##def outer(x):
##    return lambda: x**2
##print(outer(5))

##def f (i, lst=[]):
##    lst.append(i)
##    print(lst, end = " ")
##
##print(f(1))
##print(f(2))

def add_value(a):
    a += 1
    return a
b = 10
c = add_value(b)
print(c)
