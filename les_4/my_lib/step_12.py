generator = (param * param for param in range(5))

for el in generator:
    print(el)

# print(next(generator))

def generator():
    for el in (10, 20, 30):
        yield el
g = generator()
print(g)

for el in g:
    print(el)

