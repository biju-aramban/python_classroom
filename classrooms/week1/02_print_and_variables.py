# This is a comment - Mainly one line comment
"""
This is a comment - Mainly multi line comment
These structures are used to represent any kind of documentation in Python as well.
The docstrings are associated with the object as their __doc__ attribute.
These triple quotes are used to represent multiline strings as well.
"""

# The following is the import section
# The import section is used to import the required modules and packages into the current python program.
# Packages are the collection of modules.
# Modules are the collection of functions, classes and variables.
# The import section is usually placed at the top of the python program.
# The import section can be placed anywhere in the python program as well.
import os

# The following code illustrates the usage of variables in Python.
# The variables are used to store values in the memory.
# The variable names are case-sensitive.
# The variable names must start with a letter or an underscore.
# e.g. name, _name, name_1, _name_1 are valid variable names.

# The variable names can contain letters, numbers and underscores.
# e.g. name, name_1, name_1_2, name_1_2_3 are valid variable names.

# The variable names cannot start with a number.
# e.g. 1name, 1_name, 1_name_2, 1_name_2_3 are invalid variable names.

# The variable names cannot contain spaces.
# e.g. name 1, name 1 2, name 1 2 3 are invalid variable names.

# The variable names cannot contain special characters like @, #, $, %.
# e.g. name@1, name#1, name$1, name%1 are invalid variable names.

# The variable names cannot be any of the reserved keywords like print, if, else, for, while, etc.
# The variables can be declared with a value and that determines the type of the variable.
# variable types in Python are:
# int, float, str, bool, list, tuple, dict, set, frozenset, bytes, bytearray, None etc

# When you create a variable, please make sure that the variable name is meaningful.
# Examples of meaningful variable names:
# name, age, address, phone_number, email_id, is_available etc

# Variable type can be determined using the type() function.
# The following code illustrates the usage of variables in Python.

# integer variables - integer is a whole number, positive or negative, without decimals, of unlimited length.
var_int_1 = 10
var_int_2 = -21

# float variables - float is a number, positive or negative, containing one or more decimals.
var_float_1 = 0.06
var_float_2 = 20.12

# string variables - string is a collection of characters enclosed in single or double quotes
# string can contain any printable character
var_str_1 = "Hello"
var_str_2 = "World"

# boolean variables - boolean variables can have only two values - True or False
var_bool_1 = True
var_bool_2 = False

# list variables - list is a collection of items like your shopping list
var_list_1 = [1, 2, 3, 4, 5]
var_list_2 = ["a", "b", "c", "d", "e"]

# tuple variables - tuple is a collection of items as well, but it is immutable
# i.e. you cannot change the values in the tuple
var_tuple_1 = (1, 2, 3, 4, 5)
var_tuple_2 = ("a", "b", "c", "d", "e")

# dictionary variables - dictionary is a collection of key-value pairs
var_dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
var_dict_2 = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e"}

# set variables - set is a collection of unique items
var_set_1 = (1, 2, 3, 4, 5)
var_set_2 = ("a", "b", "c", "d", "e")

# frozenset variables - frozenset is a collection of unique items and it is immutable
var_frozenset_1 = frozenset({1, 2, 3, 4, 5})
var_frozenset_2 = frozenset({"a", "b", "c", "d", "e"})

# bytes variables - bytes is a collection of bytes
var_bytes_1 = b"Hello"
var_bytearray_1 = bytearray(b"Hello")

# None variable value and None means nothing is assigned to the variable.
var_none_1 = None

# The following code illustrates the usage of the print function in Python.
# The print function is used to print the output to the console.
# The print function can be used to print the values of the variables.
# The print function can be used to print the values of the variables along with message(s) that you want to print.
# When you want to print more than one value, you can use the comma (,) to separate the values.

# type() function is used to determine the type of the variable.
# Check the output for details.

print("Variables Test")
print(f"Variable: var_int_1, Value:",  var_int_1, "Variable type:",  type(var_int_1))
print(f"Variable: var_int_2, Value:",  var_int_2, "Variable type:",  type(var_int_2))
print(f"Variable: var_float_1, Value:",  var_float_1, "Variable type:",  type(var_float_1))
print(f"Variable: var_float_2, Value:",  var_float_2, "Variable type:",  type(var_float_2))
print(f"Variable: var_str_1, Value:",  var_str_1, "Variable type:",  type(var_str_1))
print(f"Variable: var_str_2, Value:",  var_str_2, "Variable type:",  type(var_str_2))
print(f"Variable: var_bool_1, Value:",  var_bool_1, "Variable type:",  type(var_bool_1))
print(f"Variable: var_bool_2, Value:",  var_bool_2, "Variable type:",  type(var_bool_2))
print(f"Variable: var_list_1, Value:",  var_list_1, "Variable type:",  type(var_list_1))
print(f"Variable: var_list_2, Value:",  var_list_2, "Variable type:",  type(var_list_2))
print(f"Variable: var_tuple_1, Value:",  var_tuple_1, "Variable type:",  type(var_tuple_1))
print(f"Variable: var_tuple_2, Value:",  var_tuple_2, "Variable type:",  type(var_tuple_2))
print(f"Variable: var_dict_1, Value:",  var_dict_1, "Variable type:",  type(var_dict_1))
print(f"Variable: var_dict_2, Value:",  var_dict_2, "Variable type:",  type(var_dict_2))
print(f"Variable: var_set_1, Value:",  var_set_1, "Variable type:",  type(var_set_1))
print(f"Variable: var_set_2, Value:",  var_set_2, "Variable type:",  type(var_set_2))
print(f"Variable: var_frozenset_1, Value:",  var_frozenset_1, "Variable type:",  type(var_frozenset_1))
print(f"Variable: var_frozenset_2, Value:",  var_frozenset_2, "Variable type:",  type(var_frozenset_2))
print(f"Variable: var_bytes_1, Value:",  var_bytes_1, "Variable type:",  type(var_bytes_1))
print(f"Variable: var_bytearray_1, Value:",  var_bytearray_1, "Variable type:",  type(var_bytearray_1))
print(f"Variable: var_none_1, Value:",  var_none_1, "Variable type:",  type(var_none_1))

# Mutliple variables can be assigned in a single line by separating them with a comma (,).
# The following code illustrates the usage of multiple variables in Python.
var_int_1, var_int_2 = 100, -210
var_float_1, var_float_2 = 0.06232, 20.1222

print("Variables Test - Multiple assignments")
print(f"Variable: var_int_1, Value:",  var_int_1, "Variable type:",  type(var_int_1))
print(f"Variable: var_int_2, Value:",  var_int_2, "Variable type:",  type(var_int_2))
print(f"Variable: var_float_1, Value:",  var_float_1, "Variable type:",  type(var_float_1))
print(f"Variable: var_float_2, Value:",  var_float_2, "Variable type:",  type(var_float_2))
