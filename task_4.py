"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
 Для решения используйте цикл while и арифметические операции.
"""

number = input(' Введите целое положительное число: ')
number = int(number)

bigger_digit = number % 10
number = number // 10


while number != 0:
    if number % 10 > bigger_digit:
        bigger_digit = number % 10
    number = number // 10
print(f'Самая большая цифра в введенном числе равна: {bigger_digit}')


