# Find the sum of all the primes below two million

def sum_primes_below(limit):
    is_prime = [True] * limit

    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p < limit:
        if is_prime[p]:
            for multiple in range (p*p, limit, p):
                is_prime[multiple] = False
        p += 1

        total = 0 
        for i in range(limit):
            if is_prime[i]:
                total += i

    return total

print(sum_primes_below(2000000))