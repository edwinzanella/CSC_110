
gapCounter = 0
comparisonCounter= 0


def insertOneGap(strng):
    global gapCounter
    gapCounter += 1
    alignments = []
    for i in range(len(strng)):
        newStrng = strng[0:i] + '-' + strng[i:len(strng)]
        alignments.append(newStrng)
    alignments.append(strng + '-')
    return alignments
            


def Union(list1, list2):
    for a in list2:
        if a not in list1:
            list1.append(a)
    return list1



def insertAllGaps(strng, gaps):
    alignments = [strng]
    for i in range(gaps):
        newAlignments = []
        for st in alignments:
            al = insertOneGap(st)
            newAlignments = Union(newAlignments,al)
        alignments = newAlignments
    return alignments


def computeScores(st, alignments):
    global comparisonCounter
    scores = []
    for al in alignments:
        score = 0
        for i in range(len(st)):
            if al[i] == '-':
                score -= 1
            elif al[i] == st[i]:
                score += 2
            else:
                score -= 2
            comparisonCounter += 1
        scores.append(score)
    return scores



def printResults(st, alignments, scores):
    print("There are ", len(alignments), " alignments")
    largestScore = max(scores)
    print("The following alignments are optimal: ")
    
    for i in range(len(alignments)):
        if largestScore == scores[i]:
            print(st)
            print(alignments[i])
            print("Score =", scores[i])
            print(" ")
    return 



        
# Main function
def main():
    # Get the two strings to align
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")

    # Compute alignments adding gaps to the shorter string
    if len(str1) > len(str2):
        longStr = str1
        shortStr = str2
    else:
        longStr = str2
        shortStr = str1

    alignments = insertAllGaps(shortStr,len(longStr)-len(shortStr))
    scores = computeScores(longStr, alignments)
    printResults(longStr, alignments, scores)
    print("Work done in adding gaps:", gapCounter)
    print("Work done in computing scores:", comparisonCounter)

    
