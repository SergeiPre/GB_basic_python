"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале
нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def sum_func(*args):
    result = 0
    out_el = False
    for el in args:
        try:
            result += float(el) if el else 0
        except ValueError as e:
            if el == 'q':
                out_el = not out_el
    return result, out_el

my_sum = 0
while True:
    sum_number = input(' Введите числа через пробел: ')
    sum_number = sum_number.split(' ')
    sum_result, out_value = sum_func(*sum_number)
    my_sum += sum_result
    print(f'Сумма: {my_sum}')
    break








