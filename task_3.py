"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
user_number = input('Введите число: ')
user_number = int(user_number)

result = (user_number + user_number * 11 + user_number * 111)
print(f'Сумма чисел равна: {result}')
