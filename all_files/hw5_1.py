def getData():
    goodFile = False
    while goodFile == False:
        fname = input("Please enter the name of the data file: ")
        try:
            infile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name, please try again ...")
    yearList = []
    totalList = []
    menList = []
    womenList = []
    line = infile.readline()
    line = infile.readline()
    while line != '':
        line = line.strip()
        years, total, men, women = line.split(',')
        yearList.append(int(years))
        totalList.append(int(total))
        menList.append(int(men))
        womenList.append(int(women))
        line = infile.readline()
    infile.close()
    return yearList, totalList, menList, womenList

def getYears(yearList):
    OK = False
    OK1 = False
    OK2 = False
    year1 = 0
    year2 = 0
    while OK == False:
        while OK1 == False:
            try:
                year1 = int(input("Enter a year: "))
                if year1 in yearList:
                    OK1 = True
                else:
                    print("Year not in range, try again...")
            except ValueError:
                print("Invalid entry, try again...")
            if year1 not in yearList:
                print("Year not in range, try again...")
        while OK2 == False:
            try:
                year2 = int(input("Enter a year: "))
                if year2 in yearList:
                    OK2 = True
                else:
                    print("Year not in range, try again...")
            except ValueError:
                print("Invalid entry, try again...")
        if year2 > year1 and year1 in yearList and year2 in yearList:
            OK = True
        else:
            print("year2 should be after year1, try again ...")
    return year1, year2

def computePercentChange(year1, year2, yearList, totalList, menList, womenList):
    total1 = 0
    total2 = 0
    men1 = 0
    men2 = 0
    women1 = 0
    women2 = 0
    for i in range(len(yearList)):
        if year1 == yearList[i]:
            total1 = totalList[i]
            men1 = menList[i]
            women1 = womenList[i]
        if year2 == yearList[i]:
            total2 = totalList[i]
            men2 = menList[i]
            women2 = womenList[i]
    totalPercent = round((total2 - total1) / (total1) * 100, 2)
    menPercent = round((men2 - men1) / (men1) * 100, 2)
    womenPercent = round((women2 - women1) / (women1) * 100, 2)
    return totalPercent, menPercent, womenPercent
            

def printResults(totalPercent, menPercent, womenPercent):
    print("Percent change overall: ", totalPercent, "%")
    print("Percent change men: ", menPercent, "%")
    print("Percent change women: ", womenPercent, "%")
    

def main():
    yearList, totalList, menList, womenList = getData()
    year1, year2 = getYears(yearList)
    totalPercent, menPercent, womenPercent = computePercentChange(year1, year2, yearList, totalList, menList, womenList)
    printResults(totalPercent, menPercent, womenPercent)
