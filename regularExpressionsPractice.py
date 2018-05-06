#!/usr/bin/python
import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#',"",phone) #this replaced '#' from phone with empty
print("Phone Num :", num)
num = re.sub(r'#.',"",phone) # this replaced '# ' from phone with empty. '.' macthes any character except new line
print("Phone Num :", num)
num = re.sub(r'#.*',"",phone) # this replaced ' # This is Phone Number' with empty. '*' repeats the re for possible number of times
print("Phone Num :", num)
num = re.sub(r'#.*$',"",phone) # '$' matches till end of the strig
print("Phone Nmm :", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    #'\D' matches non digit characters and '\d' matches only decimal digit
print("Phone Num : ", num)

#Example for lambda

def f(x):
    return x**2
print(f(8))

g = lambda x: x**2
print(g(8))

def make_inc(n):
    return lambda x:x+n
f=make_inc(2)
g=make_inc(6)

print(f(42), g(42))
print(make_inc(22)(33))

foo = [2,18,9,22,17,8,12,27]
#print(filter(lambda x: x % 3 ==0, foo))
print(map(lambda x: x * 2 + 10, foo))

