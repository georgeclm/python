import random
import secrets
import numpy as np

print(random.random())
print(random.uniform(1, 10))
# 10 is included here
print(random.randint(1, 10))
# 10 is not included
print(random.randrange(1, 10))
# deviation
print(random.normalvariate(0, 1))
mylist = list("ABCDE")
print(random.choice(mylist))
# pick unique element
print(random.sample(mylist, 2))
# this can pick the same element
print(random.choices(mylist, k=2))
random.shuffle(mylist)
print(mylist)
# store the random operation value
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

# Secrets
# 10 is not included
a = secrets.randbelow(10)
# binary value 4 mean 0-15
b = secrets.randbits(4)
alist = list('ABCDEF')
c = secrets.choice(alist)
print(a)
print(b)
print(c)

# Numpy
# Seed
np.random.seed(1)
# Numpy take dimension
print(np.random.rand(3, 3))
# 10 is excluded
print(np.random.randint(0, 10, (3, 4)))

np.random.seed(1)
print(np.random.rand(3, 3))
print(np.random.randint(0, 10, (3, 4)))

# only shuffle the x axis
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(arr)
print(arr)
