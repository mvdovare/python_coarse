#Question 13
#Level 2

#Question:
#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

input_str = input('enter characters and digits - ')

list_dig = 0
list_char = 0

for i in input_str:
    if i.isdigit():
        list_dig += 1
    else:
        list_char += 1

print('DIGITS ' + str(list_dig))
print('LETTERS ' + str(list_char))
