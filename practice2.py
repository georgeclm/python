# Practice 2 (Even Number)
class Smartphone:
    androidversion = 9.0
    screensize = "6.7 inch"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


firstphone = Smartphone("Samsung", "Rp. 5.000.000")
secondphone = Smartphone("Oppo", "Rp. 2.000.000")

print(firstphone.brand)
print(firstphone.price)
print(firstphone.androidversion, firstphone.screensize)
print(firstphone.brand, firstphone.price)
print('\r')
print(secondphone.brand)
print(secondphone.price)
print(secondphone.androidversion, secondphone.screensize)
print(secondphone.brand, secondphone.price)
