"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты
и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
sec_time = input('Введите время в секундах: ')
sec_time = int(sec_time)

minute_time = sec_time // 60
hour = minute_time // 60
minute = minute_time % 60

if minute == 0:
    second = 0
elif sec_time < 60:
    second = sec_time
else:
    second = sec_time % 60

print(f'В итоге: {hour:02d} : {minute:02d} : {second:02d}')

