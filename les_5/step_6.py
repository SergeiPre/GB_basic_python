import request

response = request.GET('https://geekbrains.ru')

# print(response)
with open('gb.html', 'w', encoding'UTF-8') as file:
    file.write(response)

print(response.headers)

response = requests.get('https://api.github.com/users/gefmar')
data = response.json()
print(data['login'])


print(response.text)


# print(response.text)
