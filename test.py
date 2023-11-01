#!/usr/bin/python3
# yob = input("year of birth: ")
# mob = input("month of birth: ")
# dob = input("day of birth: ")

# print("your date of birth is ", end='')
# print(dob, "-", mob, "-", yob)
# current_year = input("current year: ")
# age = int(current_year) - int(yob)
# result = (print(age))
# name = "love"
# print(name)
# print(name.capitalize())
# cname = (name[0].upper() + name[1:])
# print(cname)

# ace = input("what is your name")
# print(ace)

# x = 42
# if x < 0:
#     x = 0
#     print("negative change to zero")
# elif x == 0:
#     print("zero")
# elif x == 1:
#     print("single")
# else:
#     print("more")

# for n in range(2, 10):
#     #print(n)
#     for x in range(2, n):
#         #print(x)
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#     else:
#         print(n, 'is a prime number')

# light = input("what color is the light? ")
# if (light == "red"):
#     print("stop")
# elif (light == "yellow"):
#     print("get ready")
# elif (light == "green"):
#     print("go")
# else:
#     print("this color does not exist")

# i = 1
# while (i <= 10):
#     print(i)
#     i += 1
#     if (i == 6):
#         continue
#     print("hello")
# else:
#     print("counter is complete")

# name = input("name ").lower()

# vowels = " "

# for char in name:
#     if char in "aeiou":
#         vowels += char
# print("vowels in the name are: ", vowels)

# number = 3.14159
# print(f"Float: {number:.2f} Battery street")
# print("{} {}".format(number, "BatteryStreet"))

# str = "Holberton School"
# str = str * 3
# print(str)
# print(str[:9])

# str1 = "Holberton"
# str2 = "School"
# str1 = str1 + " " + str2
# print(f"Welcome to {str1}!")

# word = "Holberton"
# # word_first_3 = word[:3]
# # word_last_2 = word[7:]
# # middle_word = word[1:-1]
# word_first_3 = word[:3]
# word_last_2 = word[-2:]
# middle_word = word[1:-1]
# print(f"First 3 letters: {word_first_3}")
# print(f"Last 2 letters: {word_last_2}")
# print(f"Middle word: {middle_word}")

# str = "Python is an interpreted, interactive, object-oriented programming\
#  language that combines remarkable power with very clear syntax"
# print(str[39:66])
# print(str[])

# print(str)
# i = 1
# while (i <= 10):
#     if (i == 6):
#         i = i + 1
#         continue
#     elif (i == 7):
#         print("seven")
#     else:
#         print(i)
# else:
#     print("counter is complete\n")

#two methods of importing modules
#method 1
'''
import random
import math
for i in range(10):
    print(random.randint(1, 25))
print(math.pi)
'''
#method 2
'''
from random import randint
from math import pi
for i in range(10):
    print(randint(1, 25))
print(pi)
'''
#Aliasing module
'''
import random as rand
import math as m
import math
for i in range(10):
    print(rand.randint(1, 25))
print(m.pi)
'''

