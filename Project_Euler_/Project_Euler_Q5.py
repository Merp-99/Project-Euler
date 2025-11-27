# Smallest Multiple What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

ans = 1
for k in range(1, 21):
    ans = lcm(ans, k)

print(ans)