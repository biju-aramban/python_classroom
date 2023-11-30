# Assignment questions
# ==============

# The following problems would need the functions:
# - input()
# - print()
# - int() or float()
#
# 1. Write a program to read name of the user and age.
# Print the following details:
# Hello <user_name>, your age would be 20 in <number_of_years_to_20> years.
#
# e.g.:
# Enter your name: Jay
# Enter your age: 12
#
# Hello Jay, your age would be 20 in 8 years.
#
# 2. Write a program to read two numbers from user.
# Print the product (the numbers multiplied) in the following format.
# You have entered <number_x> and <number_y> and its product is <number_x * number_y>
#
# e.g.:
# Enter first number: 12
# Enter second number: 10
#
# You have entered 12 and 10 and its product is 120
#
# 3. Write a program to read three numbers from user.
# Print the sum (all numbers added) in the following format.
# Sum of <number_x>, <number_y> and <number_z> is <number_x + number_y + number_z>
#
# e.g.:
# Enter first number: 1
# Enter second number: 10
# Enter third number: 100
#
# Sum of 1, 10 and 100 is 111

# Answers:
# 1. Write a program to read name of the user and age.
# Print the following details:
# Hello <user_name>, your age would be 20 in <number_of_years_to_20> years.

name = input("Enter your name: ")
age = input("Enter your age: ")
# Since the input function always returns a string, we need to convert the string to the required type.
years_till_20 = 20 - int(age)
print("Hello", name, ", your age would be 20 in", years_till_20, "years.")


# 2. Write a program to read two numbers from user.
# Print the product (the numbers multiplied) in the following format.
# You have entered <number_x> and <number_y> and its product is <number_x * number_y>

number_x = input("Enter first number: ")
number_y = input("Enter second number: ")
# Since the input function always returns a string, we need to convert the string to the required type.
product = int(number_x) * int(number_y)
print("You have entered", number_x, "and", number_y, "and its product is", product)


# 3. Write a program to read three numbers from user.
# Print the sum (all numbers added) in the following format.
# Sum of <number_x>, <number_y> and <number_z> is <number_x + number_y + number_z>

number_x = input("Enter first number: ")
number_y = input("Enter second number: ")
number_z = input("Enter third number: ")
# Since the input function always returns a string, we need to convert the string to the required type.
sum_of_numbers = int(number_x) + int(number_y) + int(number_z)
# For printing the output in the required format, we can use the sep argument of the print function.
# Here we use no space as separator so that we can write properly punctuated sentences.
print("Sum of ", number_x, ", ", number_y, " and ", number_z, " is ", sum_of_numbers, sep="")

# Another way to add numbers is to use the sum function.
sum_of_numbers_2 = sum([int(number_x), int(number_y), int(number_z)])
print("Second attempt: Sum of ", number_x, ", ", number_y, " and ", number_z, " is ", sum_of_numbers, sep="")
