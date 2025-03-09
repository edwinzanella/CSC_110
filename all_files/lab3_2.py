stocks = ['IBM','AAPL','GOOG','FB','SMSN','INTC','MCD','TWTR']
stockPrices = [23.4,24.5,25.3,56.7,89.4,45.3,43.6,67.4]
findStock = input("Enter the name of the stock: ")
perIncrease = float(input("Enter the percentage increase: "))


i = 0
found = 0
while i < len(stocks) and found == 0:
    if stocks[i] == findStock:
        found = 1
        foundIndex = i
    i += 1




if found == 0:
    print("Stock not found")
else:
    finalStock = stockPrices[foundIndex] * perIncrease/100 + stockPrices[foundIndex]
    stockPrices[foundIndex] = finalStock
    print("Updated Price List:")
    print(stockPrices)

