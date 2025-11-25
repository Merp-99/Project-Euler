# Project Euler Problem 2: Even Fibonacci Numbers
# Find the sum of the even-valued terms ( which do not exceed 4mm)

prev_fib = 1
curr_fib = 2
even_sum = 2
limit = 4000000

while True:
    next_fib = prev_fib + curr_fib

    if next_fib > limit:
        break

    if next_fib % 2 == 0:
        even_sum += next_fib 

    prev_fib = curr_fib
    curr_fib = next_fib       

print(even_sum)

"""
LOGIC:
Fibonacci sequence terms are found by adding two previous terms together
N+1 = n + (n-1)
Use modulus to highlight all the even numbers
Create another variable to track the sum of even numbers found in the loop
Create a limit to only consider the values that do not exceed Four Million (stated in the question)
"""