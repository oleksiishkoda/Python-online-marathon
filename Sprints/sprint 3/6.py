from random import *
def randomWord(lst):
	while True:
		temp_lst = list(lst)
		y=0
		while y < len(lst):
			x = randint(0, len(lst) - y - 1)
			yield temp_lst[x]
			temp_lst.remove(temp_lst[x])
			y += 1
	

lst = ['hello', 'hey', 'whats', 'up ', 'yooo']
a = randomWord(lst)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print('##########')
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print('##########')
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
