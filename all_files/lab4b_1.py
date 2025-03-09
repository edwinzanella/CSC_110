def phoneNameList():
    listSize = int(input("How many names in the list: "))
    nameList = []
    phoneList = []
    i = 0
    for i in range(listSize):
        name = input("Name: ")
        phone = input("Phone: ")
        nameList.append(name)
        phoneList.append(phone)
    return nameList, phoneList, listSize

def search(phoneList, listSize):
    num = input("Enter phone number to search for: ")
    i = 0
    matched = 0
    matchedIndex = 0
    while i < listSize and matched == 0:
        if phoneList[i] == num:
            matched = 1
            matchedIndex = i
        i = i + 1
    return matched, matchedIndex

def printResults(matched, matchedIndex, nameList):
    if matched == 0:
        print("Phone number not found")
    else:
        print("Phone number belongs to " + str(nameList[matchedIndex]))
    return
    
def main():
    nameList, phoneList, listSize = phoneNameList()
    matched, matchedIndex = search(phoneList, listSize)
    printResults(matched, matchedIndex, nameList)
