import time

start = time.time()
for itm in range(0, 10**3):
    _=itm ** 2
print(time.time() - start)
