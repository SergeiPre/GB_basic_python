"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


'''Вариант 1'''
def my_func(a, b, c):
    my_list = [a, b, c]
    my_list = sorted(my_list, reverse=True)
    return my_list[0] + my_list[1]

print(my_func(1, 5, 9))

'''Ваиант 2'''
def my_func2(a, b, c):
    my_list = [a, b, c]
    new_list = []
    i = 0
    while i != 2:
        i += 1
        el = (max(my_list))
        new_list.append(el)
        my_list.remove(el)
    return sum(new_list)

print(my_func2(1, 5, 9))


