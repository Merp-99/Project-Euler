# Evaluate the sum of all the amicable numbers under 10000.

def d(n):
    if n <= 1:
        return 0
    
    total = 1
    i = 2

    while i * i <= n:
        if n % i == 0:
            total += i
            other = n // i
            if other != i:
                total += other
        
        i += 1

    return total

def sum_amicable_under(limit):
    amicable_sum = 0

    for a in range(2, limit):
        b = d(a)
        if b != a and b > 0 and d(b) == a:
            amicable_sum += a

    return amicable_sum

print(sum_amicable_under(10000))