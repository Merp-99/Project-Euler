# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    s = str(n)
    rev = s[::-1]
    return s == rev 

def largest_palindrome_product():
    largest_palindrome =  0
    for x in range(100, 1000):
        for y in range(100, 1000):
            product = x * y
            if is_palindrome(product):
                if product > largest_palindrome:
                    largest_palindrome = product
    return largest_palindrome

print(largest_palindrome_product())

"""
Ways to Improve code:
Loop from 999 downwards and a early-exit condition
Check if x or y is divisible by 11
"""

