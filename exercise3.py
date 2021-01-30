age = int(input("Your age: "))
haveDriverLicense = input("Do you have a driver license (yes/no):").lower()

if age > 21 and haveDriverLicense == "yes":
    print("You are able to drive this vehicle")
else:
    print("You are not able to drive this vehicle")
