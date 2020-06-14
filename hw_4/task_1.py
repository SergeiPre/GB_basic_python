"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, work_time, work_net_per_hour, prime_in_per_cent, *__ = argv # *__ для упаковки лишних введенных элементов
print('Выработка в часах: ', work_time)
print('Ставка (дол. в час): ', work_net_per_hour)
print(f'Премия за исполнительность в процентах от выработанных часов: {prime_in_per_cent} %')

if float(work_time) >= 176:
    result = (float(work_time) * float(work_net_per_hour)) + (float(work_time) * float(work_net_per_hour) * float(prime_in_per_cent))
else:
    result = float(work_time) * float(work_net_per_hour)

print(f' Заработная плата сотрудника с учетом премии составила {result} дол.')

