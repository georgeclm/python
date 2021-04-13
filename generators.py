import sys


def mygenerator():
    # one time use generator so went it end like looping then print it the data wont be avalible
    yield 1
    yield 2
    yield 3


# with generator it is a fixed value because they didnt store the data so same call
thegenerator = (i for i in range(1000000) if i % 2 == 0)
print(sys.getsizeof(thegenerator))
# with pure list the data keep componding
alist = [i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(alist))


def finonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b


fib = finonacci(30)
print(list(fib))


def countDow(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# by using generator no need to store a list inside the function because the generator will loop through the data and same result


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(firstn(10000)))
print(sys.getsizeof(firstn_generator(100000)))
cd = countDow(4)
value = next(cd)
print(next(cd))
print(next(cd))

g = mygenerator()
# for i in g:
#     print(i)
print(sum(g))
# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)
