# What is the largest prime factor of the number 600851475143?

n = 600851475143
factor = 2
largest_factor = 1

while factor * factor <= n:
    while n % factor == 0:
        n = n // factor
        largest_factor = factor

    if factor == 2:
        factor = 3
    else:
        factor += 2

if n > 1:
    largest_factor = n

print(largest_factor)
