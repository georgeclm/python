# if you run lambda code in this kind of type the system will transform to a function
# because lambda is normally used when you need variable instead of function and 1 time use so just store variable instead function
# this will create a function that add 10
# add10 = lambda x: x+10


# so lambda then the input argument then ":" then the output
# mult = lambda x,y: x*y
points2d = [(1, 2), (14, 2), (3, 4), (5, -2)]
# this add function key inside using lamda to sort this specific list by the index 1 or y value


def sorty_by_y(x):
    return x[1]


# this function is the same with the lambda
points2d_sorted_by_y = sorted(points2d, key=lambda x: x[1])
points2d_sorted_by_x = sorted(points2d, key=lambda x: x[0])
points2d_sorted_by_sum = sorted(points2d, key=lambda x: x[0] + x[1])


print(points2d)
print(points2d_sorted_by_y)
print(points2d_sorted_by_x)
print(points2d_sorted_by_sum)
