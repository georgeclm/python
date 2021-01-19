from collections import Counter


def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
        return b


print(10 % 5)
print(gcd(1701, 3768))
arr = [3213, 432, 123, 123, 4324, 3131]

for i in range(len(arr)):
    print(i)
# time gaming for positive : in front mean take 2 element if : in back remove 2 element from front
# opposite for negative if : in front remove 2 element from back and if : in back take 2 element from the back
s = "08:20:05PM"
tryff = 222111
print("fkasdkfmdsakf" + str(tryff))


def timeconverter(time):
    if time[-2:] == "AM" and time[:2] == 12:
        return "00" + time[2:-2]
    elif time[-2:] == "AM":
        return time[:-2]
    elif time[-2:] == "PM" and time[:2] == 12:
        return time[-2:]
    elif time[-2:] == "PM":
        return str(int(time[:2]) + 12) + time[2:8]


def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum-max(arr), sum-min(arr))


print(timeconverter(s))

a = [1, 3, 4, 5, 1, 2, 4, 5, 5, 5, 4, 4, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]


print(a.index(max(a)))


def migratoryBirds(arr):
    thearr = Counter(arr)
    result = None
    highest = 0
    for i in thearr:
        if thearr[i] > highest:
            highest = thearr[i]
            result = i
    return result


def migratoryBirds2(arr):
    bird_freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        bird_freq[arr[i]] += 1
    return bird_freq.index(max(bird_freq))


# def trynewarraylol(arr):
# for i in arr:
#    d[i] += 1
#theresult = max(d.iteritems())
# return theresult


# print(trynewarraylol(a))
print(migratoryBirds(a))
print(migratoryBirds2(a))


def newfunction(lol):
    return "22.33.{}".format(lol)


print(newfunction(662.562))
