#Edwin Hernandez-Zanella
#2/28/2023
#hw4_1

#asks the user for two lists of the abbreviation and population of states
def getStates():
    abbreviation = []
    population = []
    numOfStates = int(input("How many states are in your list? "))
    for i in range(numOfStates):
        abbreviationInput = input("Enter state abbreviation: ")
        populationInput = int(input("Enter state population: "))
        abbreviation.append(abbreviationInput)
        population.append(populationInput)
    return abbreviation, population

def searchState(abbreviation, findState):
    foundIndex = -1
    i = 0
    while i < len(abbreviation) and foundIndex == -1:
        if abbreviation[i] == findState:
            foundIndex = i
        i += 1
    return foundIndex

def higherPopStates(abbreviation, population, foundPopulation):
    higherPops = []
    for i in range(len(population)):
        if int(population[i]) > int(population[foundPopulation]):
            higherPops.append(abbreviation[i])
    return higherPops

def printResults(findState, foundPopulation, population, higherPops):
    if foundPopulation < 0:
        print("The state you entered is not valid")
    else:
        print("The population of " + findState + " is " + str(foundPopulation))
        print("The states with a higher population than " + findState + " are: ")
        print(higherPops)

def main():
    abbreviation, population = getStates()
    findState = input("Enter a state to find population of: ")
    foundIndex = searchState(abbreviation, findState)
    foundPopulation = -1
    if foundIndex >= 0:
        foundPopulation = population[foundIndex]
    higherPops = higherPopStates(abbreviation, population, foundPopulation)
    printResults(findState, foundPopulation, population, higherPops)
