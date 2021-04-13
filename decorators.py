import functools


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwds):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwds)


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwds):
        print('Start')
        result = func(*args, **kwds)
        print('End')
        return result
    return wrapper


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwds):
            for _ in range(num_times):
                result = func(*args, **kwds)
            return result
        return wrapper
    return decorator_repeat


@start_end_decorator
def addFive(x):
    return x+5


@repeat(num_times=4)
def addThree(x):
    print(int(x)+3)


@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


@CountCalls
def hello():
    print('Hello')


hello()
hello()
print(addFive(10))
addThree(10)
say_hello("John")
