import json

data = {
    'key1': [1, 2, 3],
    'key2': True,
    'key3': None,
    'key4': 'HELLO  МИР"',
    'key5': (1, 2, 3, 4),
    'key6': {'key1': [1, 2, 3],
             'key2': True,
             'key3': None,},
}

a = data['key6']['key1'][0]
print(a)

new_data = [data, data]

j_data = json.dumps(new_data, ensure_ascii=False)

print(j_data)

with open('j_data.json', 'r') as j_file:
    # json.dump(new_data, j_file)
    print(json.load(j_file))


# print(json.loads(j_data)) #loads для того чтобы взять строку
