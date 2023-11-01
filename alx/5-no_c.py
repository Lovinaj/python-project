#!/usr/bin/python3

'''
Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()
'''

def no_c(my_string):
    new_string = [i for i in my_string if i != 'c' and i != 'C']
    return(''.join(new_string))
   
    
'''or'''
# def no_c(my_string):
#     new_string = ""
#     for c in my_string:
#         if c != 'c' and c != 'C':
#             new_string += c
#     return(new_string)