#!/usr/bin/python3

import random

'''a <= x <= b'''
# a = random.randint(1, 10)
'''a <= x < b ''' 
# a = random.randrange(1, 10, 2)
'''by default floating numbers between 0 and 1 i.e 0.0 <= x < 1.0'''
# a = random.random()
'''for floating numbers'''
# a = random.uniform(1, 4) 
'''To select a random element from a sequence'''
# my_list = [1, -2, 3, -4, 5, -6, 7, 8, 9]
# a = random.choice(my_list)
'''To reorder the element of a sequence'''
# random.shuffle(my_list)
# print(my_list)
'''coding exercise 1'''
# option = random.randint(0, 1)
# if option == 1:
#     print(f"{option} is head") 
# else:
#     print(f"{option} is tail")

'''coding exercise 2
A program that select a random names from a list of names and that selected name pays the bills of everyone
'''
# team = input('enter names of team members separated by commas: ')
# team_list = team.split(',')
# print(team_list)
# team_choice = random.choice(team_list)
# print(f"{team_choice} will pay the bill")

'''OR'''
# team = input('enter names of team members separated by commas: ')
# team_list = team.split(',')
# print(team_list)
# length = len(team_list)
# team_choice = random.randint(0, length-1)
# print(f"{team_list[team_choice]} will pay the bill")


