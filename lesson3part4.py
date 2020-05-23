__author__ = 'Molodtsov Ruslan'

'''
Программа принимает действительное положительное число x
и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции
my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
'''
def power(x,y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res

print(power(float(input("First value - ")), int(input("Second value - "))))


