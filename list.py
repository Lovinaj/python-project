#!/usr/bin/python3

sea_creatures = ["shark", "squit", "mantis shrimp", "frog", "anemone"]
'''Modifying list item'''
# print(f'toad is a type of a {sea_creatures[3]}')
# print('toad is a type of a {}'.format(sea_creatures[3]))
# sea_creatures[1] = "whale"
# print(sea_creatures)
'''Slicing list'''
# print(sea_creatures[:4])
# print(sea_creatures[1:4])
# print(sea_creatures[2:4])
# print(sea_creatures[-4:-2])
print(sea_creatures[-5:])
print(sea_creatures[-5:4])

'''Slicing list including stride where the z refers to the fixed difference between each of the nubers'''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(numbers[1 : 14 : 1])
# print(numbers[0 : 14 : 3])
# print(numbers[1 : 14 : 5])
# print(numbers[::2])
'''Modifying list with operators'''
# sea_creatures = sea_creatures + ["tortise"]
# print(sea_creatures)
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']
# print(oceans * 3)
# print(sea_creatures + oceans)
# my_list = list(range(1, 4))
# print(my_list)
# for i in range(1, 4):
#     # sea_creatures += ["fish"]
#     if i == 2:
#         sea_creatures.append("toad")
#     elif i == 3:
#         sea_creatures.append("tilapia")
#     else:
#         sea_creatures.append("fish")
#     print(sea_creatures)
# sharks = ['shark']
# for x in range(1, 4):
#     sharks *= 2
#     print(sharks)
'''Removing an item from the list'''
# del sea_creatures[4]
# print(sea_creatures)
'''Construct a list with a list item'''
sea_names = [['shark', 'octopus', 'squid', 'mantis shrimp'],['Sammy', 'Jesse', 'Drew', 'Jamie']]
# print(sea_names[0][0])
# print(sea_names[0][1])
# print(sea_names[0][2])
# print(sea_names[0][3])
# print(sea_names[1][0])
# print(sea_names[1][1])
# print(sea_names[1][2])
# print(sea_names[1][3])
# print(sea_names[2][1])
# print(sea_names[2][2])
'''
How to use list method
There are 3 number of built in data structure which are list, tuples and dictionaries
They are used to manipulate datas
'''
fish = ['barracuda','cod','devil ray','eel']
fish.append("tilapia")
# print(fish)
fish.insert(2, 'anchovy')
# print(fish)
more_fish = ['goby','herring','ide','kissing gourami']
fish.extend(more_fish)
# print(fish)
fish.remove('kissing gourami')
# print(fish)
# print(fish.pop(3))
# print(fish.pop())
# print(fish)
# print(fish.index("eel"))
fish_2 = fish.copy()
# print(fish_2)
# fish.reverse()
# print(fish)
# print(fish.count('goby'))
# fish_ages = [1, 2, 4, 3, 2, 1, 1, 2, 3]
# fish_ages.sort()
# print(fish_ages)
# fish_2.clear()
# print(fish_2)
''' Using Lists as Queues. Its used to remove an item from the beginning of the list'''
# from collections import deque
# queue = deque(["john", "peter", "andrew"])
# queue.append("matthew")
# print(queue.popleft())
'''
List comprehension
syntax: list_variable = [x for x in iterable]
'''
# shark_letters = [letter for letter in 'shark']
# print(shark_letters)
# shark_letters = []

# for letter in 'shark':
#     shark_letters.append(letter)

# print(shark_letters)
'''
Using conditionals with list comprehension
List comprehensions offer a succinct way to create lists based on existing lists
Here's the basic syntax of a list comprehension: 
new_list = [expression for item in iterable if condition]

'''
# my_list = [character for character in "programming"]
# print(my_list)
'''using for loop'''
# my_string = "Hello"
# characters = []
# for char in my_string:
#     characters.append(char)
# print(characters)
'''Using conditionals with list comprehension'''
# words = ("i", "am", "learning", "python")
# my_words = [word for word in words if word != "i" if word != "am"]
# print(my_words)
# my_words = []
# for word in words:
#     if word != "i" and word != "am":
#         my_words.append(word)
# print(my_words)
'''Using mathematical operators and the range function'''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_numbers = [number for number in numbers]
# my_numbers = [number ** 2 for number in range(10) if number % 2 == 0  if number % 3 != 0]
# print(my_numbers)
'''Nested loop in list comprehension'''
# using FOR LOOP
# my_list = []
# for x in range(1, 4):
#     for y in range(1, 3):
#         my_list.append(x * y)
# print(my_list)
# '''to convert to 2x2 and 3x3 matrix'''
# result = [1, 2, 2, 4, 3, 6]
# my_matrix2 = [[result[0], result[1]], [result[2], result[3]]]
# # Convert to a 3x3 matrix
# my_matrix3 = [
#     [result[0], result[1], result[2]],
#     [result[3], result[4], result[5]],
#     [0, 0, 0]  # You can set the third row as needed
# ]

# print(my_matrix3)

'''
Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
Transpose rows and colunms 
'''
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# my_matrix = [[rows[i] for rows in matrix] for i in range(4)]
# print(my_matrix)

# Using for loop
my_matrixT = []
for i in range(4):
    matrixT = []
    for row in matrix:
        matrixT.append(row[i])
    my_matrixT.append(matrixT)
print(my_matrixT)



'''A program to check whether a year is a leap year or not'''
# year = int(input("enter year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("its is a leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("its a leap year")
# else:
#     print("its is not a leap year")


# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# Input year from the user
# year = int(input("Enter a year: "))

# Check if it's a leap year
# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

'''Nested list'''
# list = [10, 34, 90, ["mohan", "shyan", "ram"], 89]
# print(list[3][::3])

'''coding exercise
A program where one pick a position to hide money
'''
# row1 = ['😊', '😊', '😊']
# row2 = ['😊', '😊', '😊']
# row3 = ['😊', '😊', '😊']
# matrix = [row1, row2, row3]
# position = (input("where do you want to hide your money: "))
# row_number = int(position[0])
# column_number = int(position[1])
# row_selected = matrix[row_number - 1]
# row_selected[column_number-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")


