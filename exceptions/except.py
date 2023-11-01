#!/usr/bin/python3

class CustomException(Exception):
    pass


def divide(a, b):
    if b == 0:
        raise Exception("Division by zero is not allowed")
        raise CustomException("Divide by zero is not supported")
    return (a / b);

try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("You cant divide by zero");
except CustomException as e:
    # Handle another specific type of exception
    print("A custom exception occurred");
except Exception as e:
     # Handle any other exceptions
    print("An exception occurred")
finally:
    print("This will always execute");