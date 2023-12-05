# This program explains the usage of if-else statements in Python.
# if-else statements are used to make decisions in the program.
# if-else statements are also called as conditional statements.
# if-else statements are used to execute a block of code based on a condition.
# if block of code is executed if the condition is True.
# else block of code is executed if the condition is False.
# example:
# if condition:
#     block of code
# else:
#     block of code

# if number == 1:
#     print("Condition is True. Executing if block of code")
#     print("The number is 1")
#     print("if block of code is executed")
# else:
#     print("Condition is False. Executing else block of code")
#     print("The number is not 1")
#     print("else block of code is executed")

# The block of code is indented to the right by 4 spaces or a tab.
# You should use either 4 spaces or a tab for indentation. You should not mix them.
# The block of code can contain any number of statements.

# Accept a number from the user and print if the number is greater than 10 or not.
num_1 = input("Please enter a number: ")
# Convert the string to an integer
num_1 = int(num_1)

if num_1 > 10:
    print("The number", num_1, "is greater than 10")
else:
    print("The number", num_1, "is less than 10")

# Accept a name from the user
# If the name matches your name, print "Hello <name>"
# otherwise print "Sorry, I don't know you Mr <name>"
name = input("Please enter a name: ")
my_name = "Biju"

if name == my_name:
    print("Hello", name)
else:
    print("Sorry, I don't know you Mr.", name)

# When you are working with strings, please make sure that you are using the correct case.
# Python is case-sensitive. So, "Ram" and "ram" are two different strings.
# "Ram" is not equal to "ram".
# "Ram" is not equal to "RAM".
