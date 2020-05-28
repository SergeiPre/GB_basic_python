def my_f(n):
    tmp = 0
    while tmp != n:
        yield tmp ** 2
        tmp += 1

for itm in my_f(2):
    print(itm)
