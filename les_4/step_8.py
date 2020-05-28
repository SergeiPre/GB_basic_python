import sys
from my_lib.my_modul import r_sum
print(sys.argv)

_, *vars = sys.argv

tmp = [int(itm) for itm in vars if itm.isdigit()] # словарь
#tmp = {int(itm) itm for itm in vars if itm.isdigit()} # set множество
print(tmp)

print(r_sum([]))

temp = []
for itm in vars:
    if itm.isdigit():
        temp.append(itm)
print(tmp)




