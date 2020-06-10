from itertools import count

for el in count(7, 2): # (start, count)
    if el > 15:
        break
    else:
        print(el)

from itertools import cycle

с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el)
    с += 1



from itertools import cycle

progr_lang = ["python", "java", "perl", "javascript"]
iter = cycle(progr_lang)

print(next(iter), next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))


