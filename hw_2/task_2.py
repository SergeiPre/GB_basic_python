"""
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
el_num = input('Определите колличество вводимых элементов: ')
i = int(el_num)
n = 0
new_list = []

while i > 0:
    el = input('введите элемент в список: ')
    new_list.append(el)
    if i == 1:
        break
    print(new_list)
    i -= 1
print(new_list)

# new_list = ['True', 'False', '12.8', '9', '8'] # для проверки

while n < len(new_list):
    # new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
    new_list.insert(n, new_list[n + 1])
    n += 2
    new_list.pop(n)
    if len(new_list) - n == 1:
        break
print(new_list)





