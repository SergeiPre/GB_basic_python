my_tuple = [2, 4, 6]
new_obj = (el+10 for el in my_tuple)

print(new_obj)

my_dict = {el: el*2 for el in range(10, 20)}
print(my_dict)

my_set = {el**3 for el in range(10, 20)}
print(my_set)

import random
print(random.randint(10, 20))

from random import randint
print(randint(10, 20))

from random import randrange
print(randrange(10))
print(randrange(10, 20))
print(randrange(10, 20, 2))

from random import random
print(random())
print(random() * (10 - 4) + 4) # В результате получаем число от 0 до 6. Прибавляем 4 и получаем число от 4 до 10.



from random import uniform
print(uniform(10, 20)) # получаем вещественное число

from random import choice
print(choice((1, 2, 3, 4, 5, 6, 7, 8)))

import random
from random import shuffle
my_list = ["sweet", "fruits", "vegetbles"]
random.shuffle(my_list)
print(my_list)

