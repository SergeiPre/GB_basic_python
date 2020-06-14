'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce

start = 100
stop = 1000
step = 1
stop += step

new_list = [el for el in range(start, stop) if el % 2 == 0]
print(new_list)

def my_func(pre_el, folow_el):
    return pre_el * folow_el

print(reduce(my_func, new_list))


