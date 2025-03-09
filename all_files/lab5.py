# World Series Results

# Given a file with the World Series Champions since 1904
# Allow user to ask various questions about the results

def getFile():
    goodFile = False    
    while goodFile == False:
        try:
            userInput = input("Enter name of data file: ")
            infile = open(userInput, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename, please try again ... ")
    return infile

def getChamps():
    infile = getFile()
    yearList = []
    team1List = []
    team2List = []
    
    while line != '':
        line = infile.readline()
        line = line.strip()
        year, team1, team2 = line.split(',')
        yearList.append(int(year))
        team1List.append(team1)
        team2List.append(team2)   
    infile.close()
    return yearList, team1List, team2List
   
def findWinnerAndLoser(year, yearList, team1List, team2List):
    found = False
    for i in range(len(yearList)):
        if year == yearList[i]:
            found = True
            winner = team1List[i]
            loser = team2List[i]
    if found == False:
        winner = -1
        loser = -1
    return winner, loser


def getChoice():
    # This function displays the menu of choices for the user
    # It reads in the user's choice and returns it as an integer
    print("")
    print("Make a selection from the following choices:")
    print("1 - Find the World Series Winner and Loser for a particular year")
    print("2 - Count how many times a team has won the World Series")
    print("3 - Write to an output file all teams that have won the World Series")
    print("4 - Find the team that has won the most World Series Championships")
    print("5 - Find the team that has lost the most World Series Championships")
    print("6 - Quit")
    choice = int(input("Enter your choice --> "))
    print("")
    return choice


def main():    
    # Call the function to get the data from the data file and store the results in three lists
    
    yearList, team1List, team2List = getChamps()
    
    choice = getChoice()
    while choice != 6:
        if choice == 1:
            year = input("Enter the year to search for: ")
            # Call the function to get the winner and the loser
            winner, loser = findWinnerAndLoser(year, yearList, team1List, team2List)
            if winner == -1 and loser == -1:
                print("Invalid year")
            else:
                print("The " + str(winner) + " defeated the " + str(loser) + " in " + str(year))
            choice = getChoice()
        elif choice == 2:
            team = input("Enter the team name: ")
            # Call the function to get the number of wins for the team
            print(team, " won the World Series XXX times.")
            choice = getChoice()
        elif choice == 3:
            team = input("Enter the team name: ")
            # Call the function to create output file containing teams defeated by chosen team
            choice = getChoice()
        elif choice == 4:
            # Call the function to find the team that won the most championships
            print("XXX won the World Series the most at XXX times.")
            choice = getChoice()
        elif choice == 5:
            # Call the function to find the team that lost the most championships
            print("XXX lost the World Series the most at XXX times.")
            choice = getChoice()
        else:
            print("Error in your choice")
            choice = getChoice()
    print("Good-bye")
    
    
