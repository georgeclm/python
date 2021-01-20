from collections import Counter


def sockMerchant(n, ar):
    value = list(Counter(ar).values())
    theSum = 0
    for i in value:
        theSum += int(i / 2)
    return theSum
