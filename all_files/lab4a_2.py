def fact(n):
    i = n
    f = 1
    while i > 0:
        f = f * i
        i = i - 1
    return f

def comb(n, r):
    ans = round(fact(n)/ (fact(n-r) *fact(r)))
    return ans
