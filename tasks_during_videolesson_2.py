#########################################################

# Дан список. Сформировать словарь, ключами которого являются
# элементы списка, а значения равно 0.

a = ['name', 'age', 'size']

d = dict.fromkeys(a,0)
print(d)

#########################################################

# Дан список словарей с ключами name и age.
# Сформировать список имен и возрастов

spisok = [{'name':'Me', 'age':13}, {'name':'Ne', 'age':15},
          {'name':'Ve', 'age':17}]

names = []
ages = []

for a in spisok:
    names.append(a['name'])
    ages.append(a['age'])
print(names, ages)   


#########################################################

# Пользователь вводит имя, фамилию и отчество.
# Добавить словарь в список, если такого словаря еще нет.
l = [{'name':'1', 'lastname':'2', 'middlename':'3'},
     {'name':'4', 'lastname':'5', 'middlename':'6'}
    ]

name = input('ВВедите имя - ')
lastname = input('ВВедите фамилию - ')
middlename = input('ВВедите отчество - ')

d = {'name':name, 'lastname':lastname, 'middlename':middlename}

if d not in l:
    l.append(d)

l

#########################################################

# Дан список словарей с ключами name и age.
# Найти самого старшего в списке и вывести имя.

# скорей всего это другимм способом надо было сделать

spisok = [{'name':'Me', 'age':13}, {'name':'Ne', 'age':15},
          {'name':'Ve', 'age':17}]

names = ''
ages = 0

for a in spisok:
    if a['age'] > ages:
        names = a['name']
        ages = a['age']
print(names, ages)


###################################


