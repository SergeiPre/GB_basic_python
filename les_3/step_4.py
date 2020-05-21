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

for itm in temp:
    print(itm)
print('#' * 20)
print(list(temp))