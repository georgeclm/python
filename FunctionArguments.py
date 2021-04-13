def print_name(name):
    print(name)

# default value


def foo(a, b, c, d=4):
    print(a, b, c, d)


def func(a, b, *args, **kwargs):
    print(a, b)
    # array use 1 *
    for arg in args:
        print(arg)
    # dictinary 2 **
    for key in kwargs:
        print(key, kwargs[key])


def tryfunc(*args, last):
    for arg in args:
        print(arg)
    print(last)


def thefunc(a, b, c):
    print(a, b, c)


# the length must be the same in the parameter
my_list = [0, 1, 2]
my_dict = {'a': 1, 'b': 2, 'c': 3}
# unpack dictionary with **
thefunc(**my_dict)
# unpack array
thefunc(*my_list)

tryfunc(1, 2, 3, last=100)
func(1, 2, 3, 4)
func(1, 2, 3, 4, 5, six=6, seven=7)
foo(c=1, b=2, a=3)
foo(1, b=2, c=3, d=5)


def afunction():
    global number
    number = 3


number = 0

afunction()
print("after function", number)

# pass a inmutable variable will not change the global var


def fooo(x):
    x = 5

# pass in list the value from the variable will change


def data(a_list):
    # this will reference the  global list because no variable for new reference inside the local function
    a_list.append(4)
    a_list[0] = -100


def anotherdata(a_list):
    # this will not change the global var because the reference has been changed inside the function
    a_list = [1, 2, 3]
    a_list.append(4)
    a_list[0] = -100


aa_list = [1, 2, 3]
data(aa_list)
print(aa_list)
aList = [1, 2, 3]
anotherdata(aList)
# the value is not changing
print(aList)
var = 10
fooo(var)
print(var)
