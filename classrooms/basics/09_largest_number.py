# Accept N numbers from the user
# Print the largest number out of the 2 numbers
# Accept all these numbers in a single list

# Create an empty list and a counter variable
number_list = []
num_count = 10

# Loop through the counter variable
a = 1
while a <= num_count:
    num = input(f"Enter a number at {a}: ")
    num = int(num)
    number_list.append(num)
    a += 1

print("The number list: ", number_list)

# Find the largest number in the list
# Set the largest number as the first number in the list
largest = number_list[0]

# Loop through the list
for num in number_list:
    # If the number is greater than the largest number
    # Set the largest number as the number
    if num > largest:
        largest = num

print("The largest number is: ", largest)
