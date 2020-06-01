len(var_str)
10
var_str.isdigit()
False
var_str.isupper()
False
var_str.islower()
False
a = var_str
b = var_str.lower()
a
'Это строка'
и
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'и' is not defined
b
'это строка'
a is b
False
a is var_str
True
set(var_str)
{'а', ' ', 'р', 'с', 'Э', 'о', 'т', 'к'}
a = 'СТРОКА'
b = 'СТРОКА'
a is и
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'и' is not defined
a is и
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'и' is not defined
a is b
False
c = 'STRING'
d = 'STRING'
c is в
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'в' is not defined
c is d
True
id(c)
6896704
id(d)
6896704
id(a)
59111456
id(b)
59111520
a == b
True
'Это' in var_str
True
var_str[1]
'т'
len(var_str)
10
var_str[10]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: string index out of range
var_str[9]
'а'
var_str(len(var_str) - 1)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'str' object is not callable
var_str[-1]
'а'
var_str[-10]
'Э'
var_str[-11]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: string index out of range
var_str[0:4]
'Это '
var_str[0:4:2]
'Эо'
var_str[:4:2]
'Эо'
var_str[:4]
'Это '
var_str[3:]
' строка'
var_str[3:2]
''
var_str[5:1]
''
var_str[5::1]
'трока'
a = var_str
b = var_str[:]
a == и
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'и' is not defined
a == b
True
a is b
True
f = c
g == f[:]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'g' is not defined
g = f[:]
f == g
True
f is g
True
a = var_str
b = var_str[:]
a is b
True
id(a)
59841120
id(b)
59841120
var_list = [1, 2, 3, 4, 5, 'Hello', True, None, [1, 2, 3]]
var_list[1:4]
[2, 3, 4]
var_list
[1, 2, 3, 4, 5, 'Hello', True, None, [1, 2, 3]]
a = []
a
[]
var_list = list()
var_list
[]
var_list = [1, 2, 3, 4, 5, 'Hello', True, None, [1, 2, 3]]
list('Hello')
['H', 'e', 'l', 'l', 'o']
str['H', 'e', 'l', 'l', 'o']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'type' object is not subscriptable
str(['H', 'e', 'l', 'l', 'o'])
"['H', 'e', 'l', 'l', 'o']"
['H', 'e', 'l', 'l', 'o']
['H', 'e', 'l', 'l', 'o']
''.join(['H', 'e', 'l', 'l', 'o'])
'Hello'
'-:-'.join(['H', 'e', 'l', 'l', 'o'])
'H-:-e-:-l-:-l-:-o'
'H-:-e-:-l-:-l-:-o'.split('-:-')
['H', 'e', 'l', 'l', 'o']