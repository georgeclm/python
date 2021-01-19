# global variable


i = None
j = None
k = None
l = None
m = None
n = None
a = None
b = None
c = None
launch = True


def playFunc():
    opening()
    askInput()


def opening():
    print("Calculate duration of times of maximum of 59 hours and count 2 hours of count")


def askInput():
    global i, j, k, l, m, n, launch
    while launch:
        firsthour = input("Input first value with format hh:mm:ss: ")
        thefirst = firsthour.split(":")
        i = int(thefirst[0])
        j = int(thefirst[1])
        k = int(thefirst[2])
        secondhour = input("Input second value with format hh:mm:ss: ")
        thesecond = secondhour.split(":")
        l = int(thesecond[0])
        m = int(thesecond[1])
        n = int(thesecond[2])
        if i and j and k and l and m and n > 59:
            print("Invalid time input")
        else:
            runHour()
            launch = False


def runHour():
    global i, j, k, l, m, n
    if i > l:
        runSecond()
    elif i == l:
        if j > m:
            runSecond()
        elif j == m:
            if k > n:
                runSecond()
            elif k == n:
                print("Same Input")
            else:
                endgame()
        else:
            endgame()
    else:
        endgame()


def runSecond():
    global i, j, k, l, m, n, a, b, c
    if k >= n:
        c = k-n
    else:
        if j != 0:
            c = (k + 60) - n
            j -= 1


def endgame():
    pass


playFunc()
