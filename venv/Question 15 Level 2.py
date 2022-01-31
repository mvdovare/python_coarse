# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Сделал функцией чисто для того, чтобы вспомнить как пишется). Можно было просто формулу в принт например вставить.

a = str(input("enter number - "))

def formula (a):
    x = int(a) + int(a + a) + int(a+a+a) + int(a+a+a+a)
    return x

print(formula(a))
