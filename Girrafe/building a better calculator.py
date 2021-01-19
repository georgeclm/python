num1 = float(input("Enter the first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter the second number: "))
wrong = False
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "/":
    result = num1 / num2
elif op == "*":
    result = num1 * num2
else:
    result = "Operator input is invalid"
    wrong = True
if wrong:
    print(result)
else:
    print(f"The result is {result}")
