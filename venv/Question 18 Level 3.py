# Question 18
# Level 3
#
# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

import string

alphabets_lowercase = string.ascii_lowercase
alphabets_uppercase = string.ascii_uppercase
num_list = ['0','1','2','3','4','5','6','7','8','9']
char_list = ["$", "#", "@"]

resulted_pass = []

passwords = input("enter password - ").split(',')

for pass_ in passwords:
    lower_count = 0
    upper_count = 0
    num_count = 0
    char_count = 0
    for p in pass_:
        if p in alphabets_lowercase:
            lower_count += 1
        if p in alphabets_uppercase:
            upper_count += 1
        if p in num_list:
            num_count += 1
        if p in char_list:
            char_count += 1
    if char_count>=1 and len(pass_)>=6 and len(pass_)<=12 and lower_count>=1 and upper_count>=1 and num_count>=1:
        resulted_pass.append(pass_)

print(passwords)
print(resulted_pass)

