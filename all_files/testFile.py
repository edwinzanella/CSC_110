gapCounter = 0
cgapCounter = 0
comparisonCounter = 0

def insertOneGap(strng):
    global gapCounter
    newStrng = strng + '-'
    gapCounter += 1
    return newStrng

def Union(list1, list2):
    for a in list2:
        if a not in list1:
            list1 = list1 + [a]
    return list1

def insertAllGaps(strng, gaps):
    alignments = [strng]
    for i in range(gaps):
        newAlignments = []
        for st in alignments:
            al = insertOneGap(st)
            newAlignments = Union(newAlignments, [al])
        alignments = newAlignments
    return alignments

def computeScores(st, alignments):
    global comparisonCounter
    scores = []
    for i in range(len(alignments)):
        score = -1
        for j in range(len(st)):
            comparisonCounter += 1
            if alignments[i][j] == st[j]:
                score += 2
            elif alignments[i][j] == '-':
                score -= 1
            else:
                score -= 2
        scores.append(score)
    return scores

def printResults(st, alignments, scores):
    print("There are", len(alignments), "alignments")
    highestScores = max(scores)
    print("The following alignments are optimal:")
    for i in range(len(alignments)):
        if highestScores == scores[i]:
            print(st)
            print(alignments[i])
            print("Score =", scores[i], "\n")
    return

def main():
    global gapCounter, comparisonCounter
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    if len(str1) > len(str2):
        longStr = str1
        shortStr = str2
    else:
        longStr = str2
        shortStr = str1
    alignments = insertAllGaps(shortStr, len(longStr) - len(shortStr))
    scores = computeScores(longStr, alignments)
    printResults(longStr, alignments, scores)
    print("Amount of work done (gaps):", gapCounter)
    print("Amount of work done (comparisons):", comparisonCounter)

main()
