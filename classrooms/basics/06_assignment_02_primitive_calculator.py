# This program would need if - else.
# if-else statements are used to make decisions in the program.
# if-else statements are also called as conditional statements.
# if-else statements are used to execute a block of code based on a condition.
# if block of code is executed if the condition is True.
# else block of code would be executed if the condition is False.
# Note that else does not have a condition check.
# else block would be executed if none of the if block conditions are True.
#
# example:
# if <condition>:   # True or False
#      block of code
# else:
#      block of code
#
# Code # 1: (Single condition check)
# if number == 1:
#     print("Condition is True. Executing if block of code")
#     print("The number is 1")
#     print("if block of code is executed")
# else:
#       print("Condition is False. Executing else block of code")
#       print("The number is not 1")
#       print("else block of code is executed")
#
# Code # 2: (Multiple condition check)
# if number == 0:
#     print("Condition is True. Number is 0. Executing if block of code")
#     print("The number is 0")
#       print("if block of code is executed")
# elif number > 0:        # elif means else if. This helps to check another condition in the same if - elif - else block
#     print("Condition is True. Number greater than 0. Executing second if block of code")
#     print("The number is greater than 0")
#       print("Second if block of code is executed")
# else:
#       print("Condition is False. Number less than 0. Executing if block of code")    print("The number is less than 0")
#       print("if block of code is executed")
#
#
# The block of code is indented to the right by 4 spaces or a tab.
# You should use either 4 spaces or a tab for indentation. You should not mix them.
# The block of code can contain any number of statements.
#
# Question# 1
# Accept two numbers from user. Let them be x and y.
# Accept an operator. It must be one of the following: +, -, * or %
# Depending on the operator, perform the operation between numbers and print the output
# In the following format:
# Result of <operation> of <x> and <y> is: <result>.
#
# Example:
# Make sure that the message makes proper sense.
# Result of addition of 1 with 2 is: 3.
# Result of subtraction of 1 with 2 is: 1.
# Result of multiplication of 2 by 2 is: 4.
# Result of division of 2 by 2 is: 1.

print("Welcome to the primitive calculator")
print("Please enter two numbers and an operator")
print("The operator can be one of the following: +, -, * or /")

num_x = input("Enter the first number: ")
num_y = input("Enter the second number: ")
operator = input("Enter the operator: ")

num_x = int(num_x)
num_y = int(num_y)

# if
# if - else
# if (one) - elif (any number of elif-s) - else (one)

if operator == "+":
    result = num_x + num_y
    print(f"Result of addition of {num_x} with {num_y} is: {result}")

elif operator == "-":   # else if
    result = num_x - num_y
    print(f"Result of subtraction of {num_x} with {num_y} is: {result}")

elif operator == "*":
    result = num_x * num_y
    print(f"Result of multiplication of {num_x} with {num_y} is: {result}")

elif operator == "/":
    result = num_x / num_y
    print(f"Result of division of {num_x} with {num_y} is: {result}")

else:
    print("Invalid operator. Please enter either +, -, * or /")
