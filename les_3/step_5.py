def my_map(func, temp):
    for itm in temp:
        print("START")
        yield func(itm)
        print("YELD DONE")
        yield func(itm) + 15
        print('CYCLE DONE')
    return None

a = [1, 2, 3, 4, 5, 6, 7]

def my_pow(a: float) -> float: # : float необязательная функция, он возвращает значение типа float
    return a ** 2
    return result
# float это не строгасть, это пояснение
print(list(map(my_pow, a)))


temp = my_map(my_pow, [2, 3, 4, 5])
num = 22
def my_except():
    while True:

        try:
            a = input('Введите число')
            result = num / a
            print(type(a), a)

        except ValueError as error:
            print(error)
            print('Тут код ошибки!')
            continue
        except ZeroDivisionError:
            result = 0
            print('Тут код ошибки!')
            return result
        finally:
            print('Выполнится всегда')
        except Exception: # нельзя использовать в работе, люди миллионы теряли на такой строчке
            print('Hello')
    return result

result = my_exept
print('Тут код программы дальше')
print(result)
