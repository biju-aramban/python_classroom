# This is a comment - Mainly one line comment
"""
This is a comment - Mainly multi line comment
These structures are used to represent any kind of documentation in Python as well.
The docstrings are associated with the object as their __doc__ attribute.
These triple quotes are used to represent multiline strings as well.
"""

# The following is the import section
import os

# The following code illustrates the usage of variables, input and print functions in Python.
# The variables are used to store values in the memory.
# The variable names are case-sensitive and must start with a letter or an underscore.

# input function is used to read data from the user.
# input function always returns a string.
# The input function can take a prompt as an argument.

# Read the name of the user, age, and school name and print them.
name = input("Enter your name: ")
print("Hello", name)

age = input("Enter your age: ")
print("Your age is: ", age)

school_name = input("Which school do you go to: ")
print("And you go to: ", school_name)

# Since the input function always returns a string, we need to convert the string to the required type.
# if the input is an integer, we need to convert the string to an integer if we want to work with it.
number_a = input("Enter a number: ")
print("number_a is: ", number_a)
print("number_a is of type: ", type(number_a))

# Convert the string to an integer
print("Converting the string to an integer")
number_a = int(number_a)
print("number_a is: ", number_a)
print("number_a is of type: ", type(number_a))

# if the input is a float, we need to convert the string to a float if we want to work with it and so on.
number_f = input("Enter a number with a decimal point (e.g.: 10.3):")
print("number_f is: ", number_f)
print("number_f is of type: ", type(number_f))

# Convert the string to an integer
print("Converting the string to an float")
number_f = float(number_f)
print("number_f is: ", number_f)
print("number_f is of type: ", type(number_f))
