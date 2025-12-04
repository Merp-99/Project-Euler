# What is the value of the first triangle number to have over five hundred divisors?

def triangular(n):
    return n * (n+1) //2

def divisors(x):
    count = 0
    i = 1
    while i * i <=x:
        if x % i == 0:
            if i * i == x:
                count += 1
            else:
                count += 2
        i += 1
    return count
    
n = 1
while True:
    t = triangular(n)
    d = divisors(t)

    if d > 500:
        print(n, t, d)
        break
    n += 1
