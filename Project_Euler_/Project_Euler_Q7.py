# What is the 10001st prime number?

def is_prime(k):
    if k < 2:
        return False
    
    for d in range(2, k):
        if k % d == 0:
            return False
        
    return True

def nth_prime(n):
    count = 0
    number = 2 

    while True:
        if is_prime(number):
            count += 1

            if count == n:
                return number
            
        number += 1


print(nth_prime(10001))
