def bonAppetit(bill, k, b):
    bill[k] = 0
    if sum(bill) / 2 == b:
        print("Bon Appetit")
    else:
        print(abs(sum(bill) // 2 - b))
