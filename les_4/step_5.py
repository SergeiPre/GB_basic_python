all([True, False, True])
any([True, False, True])

a = [1, 0, 1, 1, 1]
b = [1, 1, 1, 1, 1]
any(b) and not all(b)

import time
time.time()

import time

start = time.time()
for itm in range(0, 10**10):
    _=itm ** 2
print(time.time() - start)
