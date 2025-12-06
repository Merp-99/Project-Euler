#Which starting number, under one million, produces the longest chain?

def collatz_length(n):
    count = 1   
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        count += 1
    return count


limit = 1000000
longest_start = 1
longest_length = 1

for i in range(1, limit):
    length = collatz_length(i)
    if length > longest_length:
        longest_length = length
        longest_start = i

print("Starting number with longest chain:", longest_start)
print("Length of chain:", longest_length)
