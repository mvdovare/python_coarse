# Пользователь вводит число
# проверить число ли было введено
# если нет - вывести текст "Enter the number please"

num = input('Введите число - ')

if num.isdigit() == False:
    print('Enter the number please')
    
###################################

# Пользователь вводит предложение
# подсчитать количество слов

sentence = input('Введите преджложение - ')

words = sentence.split()

print('Words count -', len(words))

###################################

# пользователь вводит вещественное число, 
# вывести его дробную часть

fl_num = input('Введите вещественное число - ')

znaki = fl_num.split('.')

print('вещественная часть -', znaki[1])

###################################

# пользователь вводит строку, заменить все буквы "а" на ноль

stroka = input('Введите преджложение - ')

stroka_new = stroka.replace('a', '0')

print(stroka_new)

###################################    