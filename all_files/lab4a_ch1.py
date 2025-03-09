

def fib(n):
    a = 1
    b = 2
    i = 0
    c = 0
    d = []
    while i < n and c < n:
        c = a + b
        d.append(c)
        if i % 2 == 0:
            a = c
        elif i % 1 == 0 and c < n:
            b = c
        i += 1
    return d, str(len(d))

def main(n):
    a = []
    a, b = fib(n)
    b = int(b)
    del a[b-1]
    ans = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            ans = ans + a[i]
    return ans+2
            
        
    
