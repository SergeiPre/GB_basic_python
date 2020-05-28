"""
2. Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
user_name = input('Введите ваше имя: ')
user_surname = input('Введите вашу фвмилию: ')
user_burn = input('Введите год вашего рождения: ')
user_city = input('В каком городе вы проживаете? ')
user_email = input('Введите адрес электронной почты: ')
user_number = input('Введите номер вашего телефона: ')

def second_func(user_name, user_surname, user_burn, user_city, user_email, user_number):
    print(f'имя: {user_name}; фамилия: {user_surname}; год рождения: {user_burn}; город проживания: {user_city}; email: {user_email}; телефон: {user_number}.')

print(second_func(user_name, user_surname, user_burn, user_city, user_email, user_number))