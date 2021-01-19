# sets: unordered mutable no duplicates
sets = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
othersets = {6, 7, 8, 9, 1, 2}
# other way to make sets
otherwaysets = set([3, 2, 1, 2, 5])
print(otherwaysets)
# sets that is immutable
immutablesets = frozenset([1, 2, 3, 4, 5])
print(immutablesets)
# to union
print(sets.union(othersets))
# to take the intersection
print(sets.intersection(othersets))
# to take the different from the first sets
print(sets.difference(othersets))
# to take the difference from both the sets
print(sets.symmetric_difference(othersets))
# same as union but update the sets completly
# sets.update(othersets)
# update the sets same as intersection but change the sets completly
# sets.intersection_update(othersets)
# same as difference but update the sets
# sets.difference_update(othersets)
# same as symetric update but change sets completely
# sets.symmetric_difference_update(othersets)
# this inform is all the data in sets is avalible in othersets
print(sets.issubset(othersets))
# if the sets is the same with the othersets
print(sets.issuperset(othersets))
# if the sets in sets have no same value with the othersets
print(sets.isdisjoint(othersets))
# to make a brand new sets
newset = sets.copy()
print(sets)
