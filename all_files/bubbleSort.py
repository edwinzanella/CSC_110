def bubbleSort(numList):
    for i in range(1, len(numList)):
        for j in range(len(numList) - 1):
            if numList[j] > numList[j + 1]:
                swap(numList[j], numList[j + 1])
