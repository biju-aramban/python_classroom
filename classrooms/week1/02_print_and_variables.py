import os


def variables():
    
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
    var_memoryview_1 = memoryview(b"Hello")
    var_none_1 = None
    var_path_1 = os.path.abspath(__file__)
    var_os_name_1 = os.name

    print(f"Hello {my_name}, Have a great day.")
    

if __name__ == "__main__":
    greet()
