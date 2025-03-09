def getLists():
  infile = open('awards.txt','r')
  yearList = []
  awardList = []
  winnerList = []
  line = infile.readline()
  line = line.strip()
  while line != '':
    year, award, winner = line.split(',')
    yearList.append(year)
    awardList.append(award)
    winnerList.append(winner)
    line = infile.readline()
    line = line.strip()
  infile.close()
  return yearList, awardList, winnerList

def getWinners(year, yearList, winnerList):
    yearWinners = []
    i = 0
    for i in range(len(yearList)):
        if year == yearList[i]:
            yearWinners.append(winnerList[i])
    return yearWinners
            
def outputWinners(year, yearWinners):
    print("The winners in the year " + str(year) + " were:")
    i = 0
    for i in range(len(yearWinners)):
        print(yearWinners[i])
    return 


def main():
  yearList, awardList, winnerList = getLists()
  year = input('Enter the year: ')
  yearWinners = getWinners(year, yearList, winnerList)
  outputWinners(year, yearWinners)
