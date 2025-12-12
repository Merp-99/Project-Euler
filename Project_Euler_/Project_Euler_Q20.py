# Find the sum of the digits in the number 100!.

def factorial(n):
    if n < 1 :
        raise ValueError("wrong")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

result = factorial(100)
print(result)


digit_sum = sum(int(d) for d in str(result))
print(digit_sum)
