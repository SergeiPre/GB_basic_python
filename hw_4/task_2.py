'''
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

'''

first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


for idx, item in enumerate(first_list):
    if idx and item > first_list[idx - 1]:
        result.append(item)
        print(result)



new_list = [item for idx, item in enumerate(first_list) if idx and item > first_list[idx - 1]]
print(new_list)
assert new_list == [12, 44, 4, 10, 78, 123]


