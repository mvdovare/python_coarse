# ДЗ_1


# Пользователь вводит свое имя и возраст вывести
# строку в формате - “Hello {username} your age is {age}”, 
# заменить текст в фигурных скобках на значения введенные пользователем.

username = input('Enter your name - ')
age = input('Enter your age - ')

print(f'Hello {username}, your age is {age}')

print('Hello {username}, your age is {age}'.format(username=username, age=age))

# есть ли разница или предпочтения между способами ??

#######################################################

# Пользователь вводит число, вывести его в 132 степени и 
# Показать его остаток от деления на 3. 
# Вывод должен быть в одну строку с пояснениями.

num = int(input("Please enter any number - "))
ost = num % 123
print(f'{ost} - Остаток от деления на 3 числа {num}, возведенного в 123 степень.')

#######################################################

# Пользователь вводит 2 числа вывести каждую математическую операцию для этих чисел. 
# Каждая новая операция должна быть выведена с новой строки с  пояснением.



num_1 = int(input('Please enter number 1 - '))
num_2 = int(input('Please enter number 2 - '))

print(f'Сумма веденных числе, равна - {num_1 + num_2}')
print(f'Разность первого от второго, равна - {num_1 - num_2}')
print(f'Произведение веденных числе, равна - {num_1 * num_2}')
print(f'Деление первого на второе число равно - {num_1 / num_2}')


print('Сумма веденных числе, равна - ' + str(num_1 + num_2) +
      '\nРазность первого от второго, равна -' + str(num_1 - num_2) +
      '\nПроизведение веденных числе, равна -' + str(num_1 * num_2) +
      '\nДеление первого на второе число равно -' + str(num_1 / num_2))
      
      
#########################################################
 
 # Пользователь вводит 3 числа, подставить и посчитать формулу: 2a - 8b / (a-b+c). 
# Вывести результат

a = int(input('Please enter number 1 - '))
b = int(input('Please enter number 2 - '))
c = int(input('Please enter number 3 - '))

d = 2*a-8*b / (a-b+c)
print(d)

#########################################################

# Пользователь вводит строку и число, вывести повторение строки равное введенному числу. 
# Вывод должен быть в одну строку.

st = input('Please enter a string: ')
num = int(input('Please enter the number of copies - '))

print(st*num)

#########################################################


# Даны числа 125 и 437 вывести их остатки от деления на 2, 3, 10, 22 
# с пояснениями.


li = [2,3,10,22]

for i in li:
    print(f'Остаток от деления числа 125 на {i} равно - {125 % i}')
    print(f'Остаток от деления числа 437 на {i} равно - {437 % i}')
    
### another approach ###

li = [2,3,10,22]
li2 = [125, 437]


for a in li2:
    for i in li:
        print(f'Остаток от деления числа {a} на {i} равно - {a % i}')

#########################################################


# Пользователь вводит 2 числа, 
# вывести целую часть от деления одного на другое

num_1 = int(input('Please enter number 1 - '))
num_2 = int(input('Please enter number 2 - '))

print(f'Целая часть деления одного на другое - {num_1 // num_2}')


# Пользователь  вводит 3 строки. 
# Вывести их в одну строку разделенные пробелом. 
# В этой задаче метод print может принимать только один параметр

probel = ' '
st1 = input('Please enter string - ') + probel + input('Please enter string - ' ) + probel + input('Please enter string - ')
print(st1)

#########################################################


# Даны два числа first = 15 second = 43, 
# записать first в second, a second в first. 
# Вывести

first = 15
second = 43

a = first

first = second
second = a
first, second

# а еще недавно напомнили про следующее

first, second = second, first

first, second

###################################