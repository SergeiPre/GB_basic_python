"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]

new_el = input('Введите новый элемент: ')
new_el = int(new_el)

""" Вариант 1 """
my_list.append(new_el)
print(f'Пользователь ввел натуральное число {new_el}. Результат:{sorted(my_list, reverse=True)}')


""" Вариант 2 """

# for ind, el in enumerate(my_list[:]):
#     if new_el > el:
#         my_list.insert(ind, new_el)
#         break
#     elif ind == len(my_list) - 1:
#         my_list.append(new_el)
#
# print(f'Пользователь ввел натуральное число {new_el}. Результат:{my_list}')
