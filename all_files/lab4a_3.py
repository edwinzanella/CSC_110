def sumOfMultiples(n, a, b):
    sum = 0
    i = 0
    while i < n:
        if i % a == 0 or i % b == 0:
            sum = sum + i
        i += 1
    return sum
