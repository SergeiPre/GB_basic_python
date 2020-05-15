var_str = "Это строка"
var_list = [1, 2, 3, 4, 5, 'Hello', True, None, [1, 2, 3]]
var_tuple = (1, 2, 3, 4, 5, 6, 7, 8, [1, 2, 3, 4] )
var_set = {1, 2, 3, 4, 'hello', 1, 2, 3, 4}

var_list2 = [(1, 2), (3, 4), (5, 6)]

for a, b in var_list2:
    print(a, b)


# for a, b in var_list2[::-1]:
#     var_list2.append((b, a))
#     print(a, b)


var_dict = {'KEY': 12345, 'KEY2': 'Hello'}
for key, value in var_dict.items():
    print(value)


# for itm in var_tuple:
#     print(itm)
