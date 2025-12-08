#What is the sum of the digits of the number 2^1000?

a = 2 ** 1000
a_str = str(a)

sum_a = sum(int(digit) for digit in a_str)

print(sum_a)