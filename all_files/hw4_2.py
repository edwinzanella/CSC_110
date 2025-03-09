#Edwin Hernandez-Zanella
#2/28/2023
#hw4_2


def sumDigits(n):
    list = []
    numList = []
    
    #turns number to string
    num = str(n)
    addedNum = 0

    #puts string in list
    for i in range(len(num)):
        list.append(num[i])

    #turns strings into integers
    for i in range(len(list)):
        single = int(list[i])
        numList.append(single)

    #adds the integers
    for i in range(len(numList)):
        addedNum += int(numList[i])
    return addedNum
