with open("input.txt") as f:
    digits = f.read()

digits = list(digits.rstrip())
digits = [int(digit) for digit in digits]

image_width = 25
image_height = 6
layer_area = image_width * image_height

image = [[2 for i in range(image_width)] for j in range(image_height)]

i = 0
while i < len(digits):
    layer = digits[i: i + layer_area]
    j = 0
    for digit in layer:
        if digit != 2:
            y = int(j / image_width)
            x = (j % image_width)
            if image[y][x] == 2:
                image[y][x] = digit
        j += 1
    i += layer_area

y = 0
for row in image:
    x = 0
    for digit in row:
        if digit == 0:
            image[y][x] = " "
        elif digit == 1:
            image[y][x] = "*"
        x += 1
    y += 1


for row in image:
    print("".join(row))
