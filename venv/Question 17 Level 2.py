# Question 17
# Level 2
#
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

num_tran = int(input("How many transactions - "))
d = {}
result = 0

for tran in range(num_tran):
    tran_input = input().split(' ')
    if tran_input[0] == 'D':
        result = result + int(tran_input[1])
    elif tran_input[0] == 'W':
        result = result - int(tran_input[1])
print(result)
