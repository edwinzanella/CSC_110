def matchPct(string1, string2):
    counter = 0
    if len(string1) > len(string2):
        long = string1
        short = string2
    else:
        long = string2
        short = string1
    for i in range(len(short)):
        if long[i] == short[i]:
            counter += 1
    pct = counter / len(short)
    round(pct, 2)
    return pct
