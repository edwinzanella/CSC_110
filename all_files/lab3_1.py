val = []
quit = False
warningList = []
dangerList = []
safeList = []

i = 0
while quit == False:
    vibration = float(input("Enter vibration value (-1 to quit): "))
    val.append(vibration)
    if vibration == -1:
        quit = True
        val.remove(-1)

warning = float(input("Enter threshold for warning values: "))
danger = float(input("Enter threshold for danger values: "))

while i < len(val):
    if val[i] > danger:
        dangerList.append(val[i])
    elif val[i] > warning:
        warningList.append(val[i])
    else:
        safeList.append(val[i])
    i += 1

print("There are " + str(len(safeList)) + " safe readings:")
print(safeList)
print("There are " + str(len(warningList)) + " warning readings:")
print(warningList)
print("There are " + str(len(dangerList)) + " danger readings:")
print(dangerList)

