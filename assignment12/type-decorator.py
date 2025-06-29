##--TASK 2: A Decorator that Takes an Argument--##
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"


if __name__ == "__main__":

##--TASK 1--##
    @type_converter(str)
    def my_integer_function():
        return 123

    @type_converter(float)
    def my_string_function():
        return "45.67"

    @type_converter(int)
    def my_float_function():
        return 98.76

    @type_converter(list)
    def my_tuple_function():
        return (1, 2, 3)

    print(f"my_integer_function() returns: {my_integer_function()} (type: {type(my_integer_function())})")
    print(f"my_string_function() returns: {my_string_function()} (type: {type(my_string_function())})")
    print(f"my_float_function() returns: {my_float_function()} (type: {type(my_float_function())})")
    print(f"my_tuple_function() returns: {my_tuple_function()} (type: {type(my_tuple_function())})")

    # Example with a function that takes arguments
    @type_converter(int)
    def add_numbers(a, b):
        return a + b

    print(f"add_numbers(5.5, 4.5) returns: {add_numbers(5.5, 4.5)} (type: {type(add_numbers(5.5, 4.5))})")

    y = return_int()
    print(f"return_int() returns: {type(y).__name__}") # This should print "str"
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!") # This is what should happen




