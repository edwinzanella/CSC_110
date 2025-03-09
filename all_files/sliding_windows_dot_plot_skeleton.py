# Program to compute and print a dot plot of two nucleotide sequences

# Function to find how many matches there are in two strings of equal length
def matchPct(str1, str2):
    counter = 0
    if len(str1) > len(str2):
        long = str1
        short = str2
    else:
        long = str2
        short = str1
    for i in range(len(short)):
        if long[i] == short[i]:
            counter += 1
    pct = counter / len(short)
    round(pct, 2)
    return pct


def initDotPlot(rows, cols):
    empty_dot_plot = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append("-")
        empty_dot_plot.append(row)
    return empty_dot_plot          

def computeDotPlot(str1, str2, winsize, threshold, dot_plot):
    for i in range(len(str2)):
        for j in range(len(str1)):
            pct = matchPct(str1[j:j+winsize], str2[i:i+winsize])
            if pct > threshold:
                dot_plot[i][j] = "*"


    return dot_plot

def printDotPlot(str1, str2, dot_plot):
    row = ""
    for ch in str1:
        row = row + " " + ch + " "
    print(" ", row)
    row = ""
    for i in range(len(dot_plot)):
        row = row + str2[i] + " "
        for j in range(len(dot_plot[i])):
            row = row + " " + dot_plot[i][j] + " "
        print(row)
        row = ""

# Main function
def main():
    str1 = input("Enter top string: ")
    str2 = input("Enter side string: ")
    winsize = int(input("Enter size of window: "))
    threshold = float(input("Enter expected threshold: "))
    empty_dot_plot = initDotPlot(len(str2), len(str1))
    dot_plot = computeDotPlot(str1, str2, winsize, threshold, empty_dot_plot)
    printDotPlot(str1, str2, dot_plot)

    
