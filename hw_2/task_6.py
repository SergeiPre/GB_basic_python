"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
 Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента
 — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные
у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

# commodity = [
# #     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
# #     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
# #     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# # ]
# #
# # analytics = {
# #     'название': [],
# #     'цена': [],
# #     'количество': [],
# #     'eд': []
# # }

commodities= []
dict_charcteristics = {
    'название': '',
    'цена': 0,
    'колличество': 0,
    'ед.изм.': ''}

com_count = input('Введите колличество видов товара: ')
com_count = int(com_count)

i = com_count
while i > 0:
    i -= 1
    charact_1 = input('Введите номер товара: ')
    com_number = int(charact_1)
    characteristic = dict_charcteristics.copy()

    for key in characteristic.keys():
        charact_input = input(f'Введите {key} товара(ов): ')
        if (type(characteristic[key]) is int):
            characteristic[key] = int(charact_input)
        else:
            characteristic[key] = charact_input
    commodity = (com_number, characteristic)
    commodities.append(commodity)
print('\n')
print(f'Вы определили следующие товары: \n {commodities}')
# print(commodities)

analytics = dict()

for el in commodities:
    for key, value in el[True].items():
        analytics.setdefault(f'{key}', []).append(value)
        if analytics.setdefault(key) == None:
            analytics[key] = list()
        elif value not in analytics[key]:
            analytics[key].append(value)

print('\n\n')
print(f'Analytics: \n {analytics.copy()}')
# for key, value in analytics.items():







