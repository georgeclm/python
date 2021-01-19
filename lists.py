friends = ["john", "george", "daniel", "Jonathan", "Toby"]
friends[1] = "Budi"
print(friends[-1])
# -1 mean from the back 1 which is daniel
print(friends[1:])
# to print start from index 1 until the end
print(friends[1:3])
new_friends = sorted(friends)
print(new_friends)
# to print base on order alphabetical in this list
# to end at specific index
luckyNum = [4, 3, 4, 234, 234, 234, 4, 4, 2, 4]
friends.extend(luckyNum)
# extend to add two list together
friends.append("Diane")
# to add an item  at the end of the list
friends.insert(1, "Kelly")
# to add item in specific index for the example 1 index
friends.remove("Jonathan")
# to remove the list
friends.pop()
# pop to remove the last element on the list
print(friends.index("Toby"))
# to give the index of the element
friends.clear()
# to clear the list
print(friends)
print(len(friends))
# length of the list
# make 0 5 times
mylist = [0] * 5
print(mylist)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ganjil number technique
print(a[::2])
# reverse the list
print(a[::-1])
# to copy all the list without modifying
a_copy = a[:]
print(a_copy)
square_a = [i*i for i in a]
print(square_a)
