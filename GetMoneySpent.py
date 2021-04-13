from typing import Collection, Counter


def getMoneySpent(keyboards, drives, b):
    result = []
    for i in keyboards:
        for j in drives:
            if i+j <= b:
                result.append(i+j)
    return max(result) if result else -1


def miniMaxSum(arr):
    res = []
    for i in range(len(arr)):
        arr[i] = 0
        print(arr)
        res.append(sum(arr))
    print(min(res), max(res))
    print(res)


def pickingNumbers(a):
    # Write your code here
    result = 0
    thecollect = Counter(a)
    for key, value in thecollect.items():
        result = max(result, value)
        print(key, value)
    print(list(thecollect.values())[1])

    return result


arr = [1, 2, 2, 3, 1, 2]

print(pickingNumbers(arr))
