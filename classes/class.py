#!/usr/bin/python3

class Person:
    class_variable = 'person' # class variable
    def __init__(self, name, age):
        ''' Initialize the object variable'''
        self.name = name # object variable
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and my age is {self.age}")

'''Creating an object from the "Person" class''' 
personA = Person("John", 40)

# '''Dynamically add a new attribute to the instance'''
# personA.new_name = "Peter"

# '''Access the dynamically created attribute'''
# print(personA.new_name)  # Output: "Peter"

# ''' Modifying and Accessing the class variable'''
# Person.class_variable = "Andrew"
# my_name = Person.class_variable
# print(f"my name is {my_name}")
# '''Accessing Attribute and calling a method'''
# print(personA.name)
# personA.introduce()

''' Using the getattr()'''
# name = getattr(personA, "name", None)
# age = getattr(personA, "age", None)
#state = getattr(personA, "state", None)
# print("Name:", name)
# print("Age:", age)
#print("state:", state)

''' Using the concept of Property'''

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, new_radius):
#         if new_radius >= 0:
#             self._radius = new_radius
#         else:
#             raise ValueError("Radius cannot be negative")

#     def area(self):
#         return 3.14 * self.radius ** 2

# circle = Circle(5)
# print(circle.radius)  # Access the property to get the radius
# circle.radius = 7  # Set the property to change the radius
# print(circle.radius)  # Access the property to get the updated radius
''' Dynamically create arbitrary new attributes for existing instances of a class'''
# class MyClass:
#     def __init__(self, attribute1, value):
#         self.attribute1 = attribute1
#         self.value = value

#     def __str__(self):
#         return f"MyClass instance with the value: {self.value}."
#Create an instant of a class
# obj = MyClass("value 1", 41)
# print(obj.__str__())
# print(obj.value)
# print(obj.attribute1)
# print(obj)
# Dynamically add a new attribute to the instance
# obj.new_attribute = "New Value"

# Access the dynamically created attribute
# print(obj.new_attribute)  # Output: "New Value"

class MyClass:
    class_attribute = "Class Attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    @classmethod
    def class_method(cls, arg1, arg2, arg3):
        # cls is a convention for referring to the class itself
        # You can access class-level attributes and methods using cls
        return f"Class Method called with arguments {arg1} {arg2}, and {arg3}, and class attribute: {cls.class_attribute} and {arg1.class_attribute}"

# Calling a class method without an instance
result = MyClass.class_method("arg1", "arg2", "arg3")
print(result)
