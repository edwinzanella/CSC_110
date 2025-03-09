def collectNamesSales(num):
    namesList = []
    salesList = []
    for i in range(num):
        author = input("What is the author's name? ")
        sale = int(input("How many books did they sell? "))
        namesList.append(author)
        salesList.append(sale)
    return namesList, salesList

def findHighestSales(namesList, salesList):
    highestSale = 0
    highestAuthor = ''
    for i in range(len(salesList)):
        if salesList[i] > highestSale:
            highestSale = salesList[i]
            highestAuthor = namesList[i]
    return highestAuthor

def findAverageSales(salesList):
    sumSales = 0
    for sale in salesList:
        sumSales = sumSales + sale
    averageSales = sumSales / len(salesList)
    return averageSales

def printResults(highestAuthor, averageSales):
    print("The bestselling author was " + str(highestAuthor))
    print("The average number of books sold is: " + str(averageSales))
    return

def main():
    num = int(input("How many authors are there? "))
    namesList, salesList = collectNamesSales(num)
    highestAuthor = findHighestSales(namesList, salesList)
    averageSales= findAverageSales(salesList)
    printResults(highestAuthor, averageSales)

main()