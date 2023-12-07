# This program would use while loop to draw a square.
# This program would also use if - else

# Question:
# Accept a character from the user
# Accept the size of the side of the square
# Draw a square with the character user specified.

# Example:
# Enter the fill character: *
# Enter the size of the square: 5
# Printing square:
# *****
# *****
# *****
# *****
# *****

# It may not look like a square (because how this character is drawn on the screen)
# Do you want to try drawing a rectangle and a triangle as well?

# Code:
# Printing a square
print("Let us try Printing a square...\n")
fill_char = input("Enter the fill character: ")
size = input("Enter the size of the square: ")
print("Printing square:\n")

loop_counter = 0
while loop_counter < int(size):
    # The following line prints the fill character, size number of times
    print(fill_char * int(size))
    # The following line increments the loop counter by 1
    # This is important, otherwise the loop will run forever
    # This makes sure the next line is printed in the next iteration
    loop_counter = loop_counter + 1
    # The loop condition is checked here
    # If the loop condition is true, the loop continues

# Output would look like this:
# @@@@
# @@@@
# @@@@
# @@@@

print("\nPrinting square... Completed\n")

# Printing a rectangle
print("Let us try Printing a rectangle...\n")
fill_char = input("Enter the fill character: ")
size_h = input("Enter the length of the rectangle: ")
size_v = input("Enter the height of the rectangle: ")
print("Printing rectangle:")

loop_counter = 0
# Looping through the height of the rectangle
# Height is the number of lines
while loop_counter < int(size_v):
    # The following line prints the fill character, size number of times
    # This is the width of the rectangle
    print(fill_char * int(size_h))
    # The following line increments the loop counter by 1
    loop_counter = loop_counter + 1

# Output would look like this:
# @@@@@@@@
# @@@@@@@@
# @@@@@@@@
# @@@@@@@@
print("\nPrinting rectangle... Completed\n")

print("Let us try Printing a right angle triangle...\n")
# Printing a right angle triangle
fill_char = input("Enter the fill character: ")
size_h = input("Enter the height of the triangle: ")

print("Printing right angle triangle:")
loop_counter = 1
while loop_counter <= int(size_v):
    # The following line prints the fill character, size number of times
    # This is the width of the triangle at each line
    print(fill_char * loop_counter)
    # The following line increments the loop counter by 1
    loop_counter = loop_counter + 1

# Output would look like this:
# @
# @@
# @@@
# @@@@
# @@@@@
print("\nPrinting right angle triangle... Completed\n")
