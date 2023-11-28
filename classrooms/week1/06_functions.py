# This is a comment - Mainly one line comment
"""
This is a comment - Mainly multi line comment
These structures are used to represent any kind of documentation in Python as well.
The docstrings are associated with the object as their __doc__ attribute.
These triple quotes are used to represent multiline strings as well.
"""

# The following is the import section
# The import section is used to import the required modules and packages into the current file.
import os


# The following is the function definition section
# The function definition section is used to define the functions that are used in the current file.
# The function definition section is not mandatory.
# The function definition starts with the keyword def followed by the function name and the arguments.
# The function definition ends with a colon (:)
# The function definition section is followed by the function body.
# The function body is indented by 4 spaces.
# The function body is mandatory.
# The function body is the actual code that is executed when the function is called.
# The function body can contain any valid Python code.
# The function body can contain other function definitions as well.
# The function body can contain other control structures as well.

def variables_test():
    # The following code illustrates the usage of variables in Python.
    # The variables are used to store values in the memory.
    # The variable names are case-sensitive.
    # The variable names must start with a letter or an underscore.
    # The variable names can contain letters, numbers and underscores.
    # The variable names cannot start with a number.
    # The variable names cannot contain spaces.
    # The variable names cannot contain special characters like @, #, $, %.
    # The variable names cannot be any of the reserved keywords like print, if, else, for, while, etc.
    # The variables can be declared without any type.
    # The variables can be declared with a value and that determines the type of the variable.

    # variable types in Python are:
    # int, float, str, bool, list, tuple, dict, set, frozenset, bytes, bytearray, None etc

    var_int_1 = 10
    var_int_2 = -21
    var_float_1 = 0.06
    var_float_2 = 20.12
    var_str_1 = "Hello"
    var_str_2 = "World"
    var_bool_1 = True
    var_bool_2 = False
    var_list_1 = [1, 2, 3, 4, 5]
    var_list_2 = ["a", "b", "c", "d", "e"]
    var_tuple_1 = (1, 2, 3, 4, 5)
    var_tuple_2 = ("a", "b", "c", "d", "e")
    var_dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    var_dict_2 = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e"}
    var_set_1 = {1, 2, 3, 4, 5}
    var_set_2 = {"a", "b", "c", "d", "e"}
    var_frozenset_1 = frozenset({1, 2, 3, 4, 5})
    var_frozenset_2 = frozenset({"a", "b", "c", "d", "e"})
    var_bytes_1 = b"Hello"
    var_bytearray_1 = bytearray(b"Hello")
    var_none_1 = None


    # The following code illustrates the usage of the print function in Python.
    print("Variables Test")
    print(f"Variable: var_int_1 | Value: {var_int_1} | Type: {type(var_int_1)}")
    print(f"Variable: var_int_2 | Value: {var_int_2} | Type: {type(var_int_2)}")
    print(f"Variable: var_float_1 | Value: {var_float_1} | Type: {type(var_float_1)}")
    print(f"Variable: var_float_2 | Value: {var_float_2} | Type: {type(var_float_2)}")
    print(f"Variable: var_str_1 | Value: {var_str_1} | Type: {type(var_str_1)}")
    print(f"Variable: var_str_2 | Value: {var_str_2} | Type: {type(var_str_2)}")
    print(f"Variable: var_bool_1 | Value: {var_bool_1} | Type: {type(var_bool_1)}")
    print(f"Variable: var_bool_2 | Value: {var_bool_2} | Type: {type(var_bool_2)}")
    print(f"Variable: var_list_1 | Value: {var_list_1} | Type: {type(var_list_1)}")
    print(f"Variable: var_list_2 | Value: {var_list_2} | Type: {type(var_list_2)}")
    print(f"Variable: var_tuple_1 | Value: {var_tuple_1} | Type: {type(var_tuple_1)}")
    print(f"Variable: var_tuple_2 | Value: {var_tuple_2} | Type: {type(var_tuple_2)}")
    print(f"Variable: var_dict_1 | Value: {var_dict_1} | Type: {type(var_dict_1)}")
    print(f"Variable: var_dict_2 | Value: {var_dict_2} | Type: {type(var_dict_2)}")
    print(f"Variable: var_set_1 | Value: {var_set_1} | Type: {type(var_set_1)}")
    print(f"Variable: var_set_2 | Value: {var_set_2} | Type: {type(var_set_2)}")
    print(f"Variable: var_frozenset_1 | Value: {var_frozenset_1} | Type: {type(var_frozenset_1)}")
    print(f"Variable: var_frozenset_2 | Value: {var_frozenset_2} | Type: {type(var_frozenset_2)}")
    print(f"Variable: var_bytes_1 | Value: {var_bytes_1} | Type: {type(var_bytes_1)}")
    print(f"Variable: var_bytearray_1 | Value: {var_bytearray_1} | Type: {type(var_bytearray_1)}")
    print(f"Variable: var_none_1 | Value: {var_none_1} | Type: {type(var_none_1)}")


if __name__ == "__main__":
    variables_test()
