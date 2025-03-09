purchasedItem = input("Enter name of purchased item: ")
price = int(input("Enter price of item: "))
taxRate = float(input("Enter tax rate: "))
salesTax = price * taxRate
print("The sales tax on the ", purchasedItem, " with tax rate of ", taxRate, " is:", salesTax)
