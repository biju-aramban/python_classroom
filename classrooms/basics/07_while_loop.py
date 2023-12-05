# The looping constructs
# While loop
# While loop is used to execute a block of code repeatedly as long as a condition is True.
# The condition is checked at the start of the loop.
# If the condition is True, the block of code is executed.
# The condition is checked again at the end of the loop.
# If the condition is True, the block of code is executed again.
# This continues until the condition is False.

# Modified primitive calculator to use while loop
print("Welcome to the primitive calculator")
print("Please enter two numbers and an operator")
print("The operator can be one of the following: +, -, * or /")

# To enter the loop, we need to set the condition to True
continue_looping = "y"

while continue_looping == "y":
    # Primitive calculator code
    num_x = input("Enter the first number: ")
    num_y = input("Enter the second number: ")
    operator = input("Enter the operator: ")

    num_x = int(num_x)
    num_y = int(num_y)
    result = 0

    # if the block has an if - elif - else construct, the code indented to the right one more time.
    # depending on the operator, the result is calculated
    if operator == "+":
        result = num_x + num_y
    elif operator == "-":           # elif is short for else if
        result = num_x - num_y
    elif operator == "*":
        result = num_x * num_y
    elif operator == "/":
        result = num_x / num_y
    else:
        # if the operator is not one of the 4 operators, the else block is executed
        print("Invalid operator. Please enter either +, -, * or /")

    print(f"Result of {operator} of {num_x} and {num_y} is: {result}")
    # Read the input from the user to continue or not
    continue_looping = input("Do you want to continue? (y/n): ")
    # The condition is checked at the start of the loop.

# The while loop is exited when the condition is False.
