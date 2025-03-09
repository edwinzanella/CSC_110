def fletcher32(string):
    aList = []
    bList = [0]
    checksum = 0
    for i in string:
        aList.append(ord(i))
    for i in range(len(aList)):
        bList.append((aList[i] + bList[i]) % 65535)
    for i in range(len(bList)):
        checksum = checksum + bList[i]
    checksum = checksum << 16 | max(bList)
    return checksum
