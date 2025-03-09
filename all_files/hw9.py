#Edwin Hernandez-Zanella
#hw9
#4/18/2023

#inserts a '-' between each character of strng and returns that list with the '-' in between each character
def insertOneGap(strng):
    global gapCounter
    alignments = []
    
    for i in range(len(strng)):
        newStrng = strng[0:i] + '-' + strng[i:len(strng)]
        alignments = alignments + [newStrng]
        #counter for gaps
        gapCounter += 1
        
    alignments = alignments + [strng + '-']
    
    return alignments


def Union(list1, list2):
    for a in list2:
        if a not in list1:
            list1 = list1 + [a]
            
    return list1

#inserts '-' so the two strings have the same number of characters and finds every possible arangement and puts it into the alignments list
def insertAllGaps(strng, gaps):
    global gapCounter
    alignments = [strng]
    
    for i in range(gaps):
        newAlignments = []

        for st in alignments:
            al = insertOneGap(st)
            newAlignments = Union(newAlignments,al)

        alignments = newAlignments
    return alignments

#compares each character of each element in the alignment list to st and appends the scores intoa new list to have a separate score for each string in alignments
def computeScores(st, alignments):
    global comparisonCounter
    scores = []
    
    for i in range(len(alignments)):
        score = 0
        
        for j in range(len(st)):

            if alignments[i][j] == st[j]:
                score += 2
            elif alignments[i][j] == '-':
                score -= 1
            else:
                score -=2

            #counter for comparisons
            comparisonCounter += 1
                
        scores.append(score)
        
    return scores
            
                
#prints everything
def printResults(st, alignments, scores):
    print("There are ", len(alignments), " alignments")
    highestScores = max(scores)
    print("The following alignments are optimal: ")
    
    for i in range(len(alignments)):
        if highestScores == scores[i]:
            print(st)
            print(alignments[i])
            print("Score =", scores[i])
            print(" ")
    print("Amount of work done (gaps):", gapCounter)
    print("Amount of work done (comparisons):", comparisonCounter)
    
    return


def main():
    #defines global variables
    global gapCounter, comparisonCounter
    gapCounter = 0
    comparisonCounter = 0

    #user input
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")

    #sets the longer string to longStr
    if len(str1) > len(str2):
        longStr = str1
        shortStr = str2
    else:
        longStr = str2
        shortStr = str1

    #calls functions
    alignments = insertAllGaps(shortStr,len(longStr)-len(shortStr))
    scores = computeScores(longStr, alignments)
    printResults(longStr,alignments, scores)
