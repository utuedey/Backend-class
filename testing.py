def say_hello_before_running(func):
    """
    This is our simple decorator function.
    It takes another function (func) as input.
    """
    def wrapper():
        print("Hello! I'm about to run your function!") # New behavior added by decorator
        func() # Now, run the original function
        print("I just finished running your function!") # More new behavior
    return wrapper

# Now, let's use our decorator!
@say_hello_before_running
def my_regular_function():
    print("This is my regular function doing its job.")

# When we call my_regular_function, it's actually calling the 'wrapper'
my_regular_function()