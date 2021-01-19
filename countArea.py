# global variable

valid = True
result = None
shape = None


def playCount():

    opening()
    selector()
    announceResult()


def selector():
    global valid, result, shape
    while valid:
        theArea = input(
            "Input what shape you want to count the area \n (a) Circle \n (b) Rectangle \n (c) Triangle\n")
        if theArea == "a":
            result = countCircle()
            shape = "circle"
            valid = False
        elif theArea == "b":
            result = countRectangle()
            shape = "rectangle"
            valid = False
        elif theArea == "c":
            result = countTriangle()
            shape = "triangle"
            valid = False
        else:
            print("False input")


def opening():
    print("This code is to count area of the chosen shape")


def announceResult():
    print(f"So the area of your {shape} is {result}")


def countCircle():
    x = int(input("Input the radius of the circle: "))
    return 3.14 * x * x


def countRectangle():
    x = int(input("Input the length of your rectangle: "))
    y = int(input("Input the width of your rectangle: "))
    return x * y


def countTriangle():
    x = int(input("Input the base of your triangle: "))
    y = int(input("Input the height of your triangle: "))
    return 0.5 * x * y


playCount()
