# Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

inp_str = input("Enter words - ")
Uppercases = 0
Lowercases = 0
#inp_str.replace(" ", "")
for i in inp_str.replace(" ", ""):
    if i.isupper():
        Uppercases += 1
    else:
        Lowercases += 1

print("Uppercases - " + str(Uppercases) + "\n" + "Lowercases - " + str(Lowercases))
