# Project Euler Problem 1: Multiples of 3 and 5:
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(k, limit):
    m = (limit - 1) // k
    return k * m * (m + 1) // 2

answer = (
    sum_of_multiples(3, 1000)
    + sum_of_multiples(5, 1000) 
    - sum_of_multiples(15, 1000)
)

print(answer)