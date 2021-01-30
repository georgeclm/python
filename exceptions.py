x = -5
if x > 0:
    raise Exception
# assert(x >= 0), 'x is not positive'
try:
    a = 5/0
except ZeroDivisionError as e:
    print(e)
