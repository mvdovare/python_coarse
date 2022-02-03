# Question 19
# Level 3
#
# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.
from operator import itemgetter

l = []
i = 0

resulted_list = []
while i < 4:
    d = {}
    raw_input = input("enter values - ").split(",")
    d['name'] = raw_input[0]
    d['age'] = int(raw_input[1])
    d['height'] = int(raw_input[2])
    l.append(d)
    i += 1

l_sort = sorted(l, key=itemgetter ('name', 'age', 'height'), reverse=False)
for one_dict in l_sort:
    t = []
    t.append(one_dict['name'])
    t.append(one_dict['age'])
    t.append(one_dict['height'])
    T1 = tuple(t)
    resulted_list.append(T1)

print(resulted_list)