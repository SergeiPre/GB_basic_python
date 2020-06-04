import sys
from my_lib.my_modul import r_sum
print(sys.argv)

_, *vars = sys.argv

tmp = tuple(itm for itm in vars if itm.isdigit())
print(tmp)

print(r_sum([]))

temp = []
for itm in vars:
    if itm.isdigit():
        temp.append(itm)
print(tmp)




