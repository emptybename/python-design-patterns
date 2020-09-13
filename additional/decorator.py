# # First we assign function to a variable
# def plus_one(number):
#     return number + 1
#
#
# add_one = plus_one
# print(add_one(4))
#
#
# # End
#
#
# # Defining function inside another function
# def plus_one(number):
#     def add_one(number):
#         return number + 1
#
#     result = add_one(number)
#     return result
#
#
# print(plus_one(5))
#
# # End

# Passing Functions as Arguments to other Functions
def add_one(number):
    return number + 1


def plus_one(function):
    number = 6
    return function(number)


print(plus_one(add_one))


# End


# Function returning other function
def hello_function():
    def say_hi():
        print("Hi")

    return say_hi


hello = hello_function()
hello()


# End

# Nested Functions have access to the Enclosing Function's Variable Scope
def print_message(message):
    # Enclosing function
    def message_sender():
        # Nested function
        print(message)

    message_sender()


print_message("Hi Mayank")


# End

# Creating Simple decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        upper_case = func.upper()
        return upper_case

    return wrapper


def say_hi():
    return "hello there"


decorator = uppercase_decorator(say_hi)
print(decorator())


# OR we can do it in pythonic way

@uppercase_decorator
def hello():
    return "Hello Mayank"


print(hello())


def split_string(function):
    def wrapper():
        func = function()
        return func.split()

    return wrapper


@split_string
@uppercase_decorator
def print_hello():
    return "hello world"


print(print_hello())


# End

# Accepting Arguments in Decorator Functions

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)

    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city1, city2):
    print(city1, city2)


cities("gwalior", "indore")


# End


# Passing Arguments to the Decorator
def decorator_maker_with_arguments(d_arg1, d_arg2):
    def decorator_func(function):
        def wrapper(func_arg1, func_arg2):
            print("decorator arguments - ", d_arg1, d_arg2)
            function(func_arg1, func_arg2)

        return wrapper

    return decorator_func


@decorator_maker_with_arguments("Pandas", "Numpy")
def decorated_function_with_arguments(arg1, arg2):
    print("Decorated function arguments - ", arg1, arg2)


decorated_function_with_arguments("hello", "world")
# End
