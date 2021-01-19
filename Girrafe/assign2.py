# global variable
import math
x1 = None
x2 = None
a = None
b = None
c = None
d = None


def main():
    opening()
    askInput()
    seperator()
    announce()


def opening():
    print("The format is ax^2+bx+c")


def askInput():
    global a, b, c, d
    thedata = input("Input the value of a, b  and c split by space: ")
    thesplit = thedata.split()
    a = int(thesplit[0])
    b = int(thesplit[1])
    c = int(thesplit[2])

    d = (b*b) - (4*a*c)


def seperator():
    global x1, x2, d
    if d == 0:
        x1 = -b / (2*a)
        x2 = x1
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)


def announce():
    global d, x1, x2
    if d == 0 or d > 0:
        print("X1 root: {}".format(x1))
        print("X2 root: {}".format(x2))
    else:
        print("Imaginary Numbers")


main()
