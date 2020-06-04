a = [1, 2, 3, 4, 5]

def my_func2(temp: list) -> float:
    temp.append(2345)
    print(temp)
    return temp

def my_pow(a: float) -> float: # : float необязательная функция, он возвращает значение типа float
    return a ** 2
    return result
# float это не строгасть, это пояснение
print(list(map(my_pow, a)))

def my_func3(a, b, c, d):
    return sum(a, b, c, d)


print(a)
result = my_func2(a)
result = my_func3(b=2, c=3, a=6, d=17)
print(a)
print(result)

m_d = {
    'a': 2,
    'b': 3,
    'c': 4,
    'd': 5, # ',' - нужна чтобы не породить ошибок в коде
}

def my_max(*args, **kwargs):
    print('KWARGS', type(kwargs))
    print(kwargs)
    print('KWARGS', type(args))
    result = float('inf') * -1
    for itm in args:
        if result < itm:
            result = itm
    return result


m_l = [2, 3, 4, 5, 4, 5, 5, 6]

result = my_max(1, 2, 3, 4, 5, 22, 66, 1, 3, 77, 87, 222, 33, key=my_pow)
result = my_func3(*m_l[:4])
result = my_func3(**m_d)

print(result)


a, b, c, *d = input('Hello'.split(' ')) # *d - может принять множество значений
print(a, b, c, d)

print(m_l)


# анонимные функции

lambda x: x ** 2

# тернанрная операция

temp = 22 if b > 0 else 33
list(map(lambda x: x ** 2 if not x % 2 else x ** 3, a))
#[1, 4, 27, 16, 125, 36, 343]
list(map(lambda x: x ** 2 if not x % 2 else x ** 3, a[:3]))
#[1, 4, 27]
list(map(lambda x: x ** 2 if not x % 2 else x ** 3, a[:4]))
#[1, 4, 27, 16]

# True or False
# #True
# '' or 0 # возвращает последний встречный true
# #0
# '' and 1 # возвращает первый встречны false
# #''

