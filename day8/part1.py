from collections import Counter

with open("input.txt") as f:
    digits = f.read()

digits = list(digits.rstrip())

image_width = 25
image_height = 6
layer_area = image_width * image_height

digit_counts = dict()
for digit in set(digits):
    digit_counts[digit] = -1

i = 0
while i < len(digits):
    layer = digits[i: i + layer_area]
    counts = Counter(layer)

    if digit_counts['0'] == -1:
        for digit in digit_counts.keys():
            if digit in counts.keys():
                digit_counts[digit] = counts[digit]
            else:
                digit_counts[digit] = 0
    else:
        if counts['0'] < digit_counts['0']:
            for digit in digit_counts:
                if digit in counts.keys():
                    digit_counts[digit] = counts[digit]
                else:
                    digit_counts[digit] = 0
    i += layer_area

print(digit_counts['1'] * digit_counts['2'])