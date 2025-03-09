list1 = [1,4,6,7,9,11,15]
list2 = [2,3,4,5,10,11,12] 
list1.extend(list2)
sortList = []

i = 0
a = 0
while i < len(list1):
    numList = list1.count(a)
    if numList >= 1:
        b = 0
        while b < numList:
            sortList.append(a)
            list1.remove(a)
            b = b + 1
    else:
        a = a + 1

print(sortList)
