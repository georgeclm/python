from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator
# this to iterate a to b to x,y in value print the possible meet
a = [1, 2]
b = [3]
# use repeat to repet the product meet 2 times
prod = product(a, b, repeat=2)
print(list(prod))
print("gappp")
# permutations
# the permutation print the posiible 3 meet and for permutation if different order then new permutate
c = [1, 2, 3]
perm = permutations(c)
# only take 2 value
print(list(permutations(c, 2)))
print(list(perm))
# combinations
d = [1, 2, 4, 3]
comb = combinations(d, 2)
print(list(comb))
# this is for combination with replacement so all same value 1,1 ; 2,2 ; 3,3 and etc
comb_wr = combinations_with_replacement(d, 2)
print(list(comb_wr))
# accumulate
# this accumalate to plus each part
acc = accumulate(d)
print(list(acc))
# this the multiplication accumulate
print(list(accumulate(d, func=operator.mul)))
# this take the maximum went reach until the last array
print(list(accumulate(d, func=max)))
# groupby


def smaller_than_3(x):
    return x < 3


# this group by function to split the function and still using the key which give boolean and split the value depend on the key
f = [1, 2, 3, 4]
# create a collection so the same key and value
# this lambda function make it faster by creating parameter and return a boolean
groupobj = groupby(f, key=lambda x: x < 3)
# same result as below with the smalller than function
# groupobj = groupby(f, key=smaller_than_3)
# for the key it will be the value inside lambda
for key, value in groupobj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'John', 'age': 25},
           {'name': 'George', 'age': 25}, {'name': 'Jenn', 'age': 33}]


otherobj = groupby(persons, key=lambda y: y['age'])
for key, value in otherobj:
    print(key, list(value))

# count function

jannn = [1, 2, 3]
# the count method mean the number will start from the number and will keep counting
for i in count(10):
    print(i)
    if i == 15:
        break
# this will cycle through the list this is infinite loops
# for i in cycle(jannn):
#   print(i)
# this repeat mean it will repeat the 1 for 4 times
for i in repeat(1, 4):
    print(i)
