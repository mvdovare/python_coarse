#Question 2
#Level 1

#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line. Надо просто ввод и результат?
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

number = input ("Please enter your number - ")

i = 1
result = 1
output = []
while i < int(number):
    result = result * (i+1)
    i+=1
print (result)
