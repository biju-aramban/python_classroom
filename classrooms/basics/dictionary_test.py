
filename = r"D:\workspace\github\python_classroom\classrooms\basics\names.txt"

f_reader = open(filename, "r")
names = f_reader.readlines()
f_reader.close()

number_of_names = len(names)
index = 0
dict_names = dict()
while index < number_of_names:
    names[index] = names[index].strip()
    name = names[index]
    if name in dict_names:
        dict_names[name] += 1
    else:
        dict_names[name] = 1

    index += 1

print("The names: ", names)
print("The dict_names: ", dict_names)
