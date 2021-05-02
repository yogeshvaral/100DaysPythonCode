import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()

    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def greeting():
    print("Good Morning")


def sayBye():
    print("Bye")

say_hello()
greeting()
sayBye()