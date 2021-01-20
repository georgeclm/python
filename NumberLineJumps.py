def kangaroo(x1, v1, x2, v2):
    meet = True
    if x2 > x1 and v2 > v1:
        return "NO"
    while(meet):
        if x1 == x2:
            meet = False
            return "YES"
        x1 += v1
        x2 += v2
        if x1 > 99999999 or x2 > 99999999:
            meet = False
            return "NO"
