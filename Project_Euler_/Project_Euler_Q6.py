# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = 0
sum_of_numbers = 0 

for number in range(1, 101):
    sum_of_squares += number * number

for number in range(1, 101):
    sum_of_numbers += number

square_of_sum = sum_of_numbers * sum_of_numbers

print(square_of_sum - sum_of_squares)

