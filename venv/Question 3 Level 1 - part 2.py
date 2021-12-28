#Question 3
#Level 1

#Question:
#With a given integer number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral #number between 1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.
#Consider use dict()

number_input = input('enter number - ')
result_dict = {}
number_2 = 0
i = 1
try:
    int(number_input).isdigit() == True
    number_2 = int(number_input)
    while i <= number_2:
        result_dict.update({i: i * i})
        i += 1
    print(result_dict)
except:
    print('You entered not digits, bye bye')


