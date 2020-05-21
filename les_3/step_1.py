a = [1, 2, 3, 4, 5, 6, 7]
max(a)

min(a)

pow(3, 3) # возвести в 3 степень

result = []

for itm in a:
    result.append(pow(itm, 2))
    print(result)

# list(map(pow, a)) # ошибочно

def my_pow(a: float) -> float: # : float необязательная функция, он возвращает значение типа float
    return a ** 2
    return result
# float это не строгасть, это пояснение
print(list(map(my_pow, a)))





