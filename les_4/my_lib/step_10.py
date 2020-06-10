# import time
# import random
#
# print(time.time())
# print(random.random())

from time import time
from random import random

print(time())
print(random())



my_list = [2, 4, 6]
new_list = [el+10 for el in my_list]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

my_list = [2, 4, 6]
print(f"Исходный список: {my_list}")
new_list = []
for el in my_list:
   new_list.append(el + 10)
print(f"Новый список: {new_list}")

lines = [line.strip() for line in open('text.txt')]
print(lines)


my_list = [10, 25, 30, 45, 50]
print(my_list)
new_list = [el for el in my_list if el % 2 == 0]
print(new_list)

str_1 = "abc"
str_2 = "d"
str_3 = "efgklm"
sets = [i+j+k for i in str_1 for j in str_2 for k in str_3]
print(sets)






