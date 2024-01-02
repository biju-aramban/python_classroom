# Accept 2 numbers from the user
# Print the largest number out of the 2 numbers
# Accept all these numbers in a single list

number_list = []
num_count = 4

a = 0
while a < num_count:
    num = input("Enter a number: ")
    num = int(num)
    number_list.append(num)
    a += 1

print("The number list: ", number_list)
largest = number_list[0]

for num in number_list:
    if int(num) > largest:
        largest = int(num)

print("The largest number is: ", largest)
