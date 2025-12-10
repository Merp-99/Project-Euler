ONES = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen",
}

TENS = {
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
}

def two_digit_words(n):
    # Handles everything from 1 to 99
    if n < 20:
        return ONES[n]
    if n in TENS:
        return TENS[n]
    return TENS[n // 10 * 10] + "-" + ONES[n % 10]

def three_digit_words(n):
    # Splits 342 into "three hundred" + "and" + "forty-two"
    hundreds = n // 100
    remainder = n % 100

    base = ONES[hundreds] + " hundred"
    if remainder == 0:
        return base
    return base + " and " + two_digit_words(remainder)

def number_to_words(n):
    if n == 1000:
        return "one thousand"
    if n < 100:
        return two_digit_words(n)
    return three_digit_words(n)

# Count letters
total = 0
for n in range(1, 1001):
    w = number_to_words(n)
    cleaned = w.replace(" ", "").replace("-", "")
    total += len(cleaned)

print(total)