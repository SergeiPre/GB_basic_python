
file = open('input.txt', 'r', encoding='UTF-8') # в скобках передаем путь к файлу ввиде строки

for line in file:
    print(line, end='')

print(file.readlines())

print(file.readline(8))

print(file.readline(8))
