"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
 возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
""" Вариант 1 """

def my_func(x, y):
    return x ** y

print(my_func(100, -2))

""" Вариант 2 """

def my_func2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


print(my_func2(100, -2))


''' Вариант 3'''
from functools import reduce

def my_multip(x, y):
    result = 0
    for _ in range(y):
        result += x
    return result


def my_func(x: float, y: int):
    result = 1
    for _ in range(abs(y)):
        result = my_multip(result, x)
    return result if y > 0 else 1 / result