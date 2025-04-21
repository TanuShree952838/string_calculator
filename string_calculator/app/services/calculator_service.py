import re

def add_numbers(numbers_str: str):
    if not numbers_str:
        return 0, []

    delimiter = ",|\n"
    if numbers_str.startswith("//"):
        parts = numbers_str.split("\n", 1)
        delimiter = re.escape(parts[0][2:])
        numbers_str = parts[1]

    numbers = re.split(delimiter, numbers_str)
    total = 0
    negatives = []

    for num in numbers:
        if num.strip():
            n = int(num)
            if n < 0:
                negatives.append(n)
            total += n

    return total, negatives
