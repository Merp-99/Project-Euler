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

"""
LOGIC:
Find the sum of multiples of 3 and 5. 
You can't add the multiples as they share some numbers and would inflate the number.
To fix this, you can take away one set of the shared multiples which is the sum of multiples of 3 and 5.
The answer will be sum of 3 and sum of 5 - sume of 15 (all below the limit of 1000)
"""