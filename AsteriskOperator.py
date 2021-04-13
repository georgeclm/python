# * * * * *
result = 5**7
# list
zeros = [0, 1] * 10
# tuple
zeros = ('ab') * 10


def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


numbers = [1, 2, 3, 4, 5, 6]
# will always unpack to list even tuple
beginning, *middle, secondlast, last = numbers
print(beginning)
print(middle)
print(secondlast)
print(last)
foo(1, 2, 3, 4, 5, six=6, seven=7)
print(zeros)
print(result)

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)
# join a dictionary
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
new_dict = {**dict_a, **dict_b}
print(new_dict)
