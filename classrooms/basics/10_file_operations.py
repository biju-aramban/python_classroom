# File Operations
# Files are used to store information in the form of text, binary, and other formats on hard disk.
# Python provides various functions to perform file operations.
# open() function is used to open a file. It returns a file object, also called a handle, as it is used to read or modify the file.

# Syntax:
# file_object = open(file_name, access_mode)
# file_name: The file_name argument is a string value that contains the name of the file that you want to access.
# access_mode: The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc.

# Different modes of opening a file:
# r: Opens a file for reading. (default)
# w: Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# a: Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# x: Opens a file for exclusive creation. If the file already exists, the operation fails.

import time
record_file = r"C:\temp\test.txt"

# Open a file in read mode and read all the content
f_reader = open(record_file, "r")
# This returns the file content
records = f_reader.read()
f_reader.close()

# print(records)

# Open a file in read mode and read the file line by line.
# Works for text files and not for binary files
f_reader = open(record_file, "r")

while True:
    # this returns a line from the file
    record = f_reader.readline()
    if not record:
        break

    time.sleep(2)
    print(record.strip())

f_reader.close()

# Open a file in read mode and read all the lines.
f_reader = open(record_file, "r")
# this returns a line from the file
records = f_reader.readlines()
f_reader.close()

print(records)

write_record_file = r"D:\workspace\github\python_classroom\classrooms\basics\beme_write_records.txt"
# Open a file in write mode and write into it.
f_writer = open(write_record_file, "w")     # "a" for append
# this returns a line from the file
f_writer.write("Hello world\n")
f_writer.write("Hello another world\n")
f_writer.close()

f_reader = open(write_record_file, "r")
# this returns a line from the file
records = f_reader.readlines()
f_reader.close()
print(records)
