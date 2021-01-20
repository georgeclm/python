def countApplesAndOranges(s, t, a, b, apples, oranges):
    arrapple = []
    arrorange = []
    totalapple = 0
    totalorange = 0
    for i in apples:
        arrapple.append(a + i)
    for i in oranges:
        arrorange.append(b + i)
    for i in arrapple:
        if i >= s and i <= t:
            totalapple += 1

    for i in arrorange:
        if i >= s and i <= t:
            totalorange += 1

    print(totalapple)
    print(totalorange)
