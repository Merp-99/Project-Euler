# What is the total of all the name scores in the file?

with open("0022_names.txt") as file:
    data = file.read()

names = data.replace('"', '').split(',')
names.sort()

def name_value(name):
    total = 0
    for letter in name:
        total += ord(letter) - 64
    return total

total_score = 0

for index, name in enumerate(names, start=1):
    total_score += index * name_value(name)

print(total_score)
