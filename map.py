from functools import reduce
# map (func,seq)
a = [1, 2, 3, 4]
# multiply all element by 2
b = map(lambda x: x*2, a)
print(list(b))
# same result
c = [x*2 for x in a]
print(c)
# filter(func,seq)
# take the even number
d = filter(lambda x: x % 2 == 0, a)
print(list(d))
# same result
e = [x for x in a if x % 2 == 0]
print(e)
# reduce(func,seq)
# to take all value multiple all
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
