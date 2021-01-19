# Collection
from collections import Counter, namedtuple, defaultdict, deque

a = "aaaabbbccc"
b = Counter(a)
# this is to print the values which mean the count

print(b.values())
# this keys to print out the key that is going to get printed out value
print(b.keys())
# to take the most common element or the most element that is getting called
# use index 0 to take the first item because it is tuple
# the second index 0 to take the keys and 1 to take the value
print(b.most_common()[0][0])
print(list(b.elements()))

# named Tuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)
# ordered Dict
ordered_dict = {}
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1

print(ordered_dict)
# default dict the difference is they the default dictionaries have default value
# the default value of an integer is 0
d = defaultdict(int)
# the default of list is empty so wont raise error
# d = defaultdict(list)

d['a'] = 1
d['b'] = 2
print(d['c'])

# deque just like the name a deck
e = deque()
e.append(1)
e.append(2)
# to append an element from the left
e.appendleft(3)
print(e)
# remove the last element and use popleft to remove the first
e.pop()
print(e)
# remove all
e.clear()
print(e)
# to extend and extendleft to extend from the first
e.extendleft([4, 5, 6])
print(e)
# rotate element to the right 1 time and minus number to rotate to the left
e.rotate(1)
print(e)
