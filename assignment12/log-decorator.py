# Step 1
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    """
    A decorator that logs information about the function being called,
    including its name, arguments, and keyword arguments.
    """
    def wrapper(*args, **kwargs):
        # Log the name of the function being executed.
        logger.info(f"Function name: {func.__name__}")

        # Log the positional arguments if any are present.
        if args:
            logger.info(f"  Arguments: {args}")

        # Log the keyword arguments if any are present.
        if kwargs:
            logger.info(f"  Keyword arguments: {kwargs}")

        # Call the original function with its arguments and keyword arguments.
        result = func(*args, **kwargs)

        # Log the value returned by the function.
        logger.info(f"  Returned: {result}")

        # Return the result of the original function so the decorated function behaves as expected.
        return result
    return wrapper

# --- Function Declarations (Decorated) ---

# 1. Function that takes no parameters and returns nothing.
@logger_decorator
def greet_world():
    print("Hello, World!")

# 2. Function that takes a variable number of positional arguments and returns True.
@logger_decorator
def sum_all_numbers(*numbers):
    print(f"Numbers received: {numbers}")
    total = sum(numbers)
    print(f"Sum: {total}")
    return True

# 3. Function that takes no positional arguments and a variable number of keyword arguments,
#    and that returns logger_decorator itself.
@logger_decorator
def configure_settings(**settings):
    print(f"Configuration settings received: {settings}")
    return logger_decorator

if __name__ == "__main__":
    print("--- Calling greet_world() ---")
    greet_world()

    print("\n--- Calling sum_all_numbers() ---")
    sum_all_numbers(1, 2, 3)
    sum_all_numbers(10, 20, 30, 40, 50)
    sum_all_numbers() # Call with no arguments

    print("\n--- Calling configure_settings() ---")
    returned_decorator = configure_settings(theme="dark", font_size=12, enable_notifications=True)
    print(f"Returned from configure_settings: {returned_decorator}")


    print("\n--- Program execution complete. Check 'decorator.log' for details. ---")



