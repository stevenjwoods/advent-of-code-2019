import sys

with open("input.txt") as f:
    paths = f.readlines()

paths = [path.rstrip().split(",") for path in paths]
x = 0
y = 0

path1 = dict()
path1[0] = [0]

for instruction in paths[0]:
    direction, distance = instruction[0], int(instruction[1:])
    if direction == "R":
        try:
            path1[y] += [x+i+1 for i in range(distance)]
            x += distance
        except KeyError:
            path1[y] = [x+i+1 for i in range(distance)]
            x += distance
    elif direction == "L":
        try:
            path1[y] += [x-i-1 for i in range(distance)]
            x -= distance
        except KeyError:
            path1[y] = [x-i-1 for i in range(distance)]
            x -= distance
    elif direction == "U":
        for i in range(distance):
            try:
                path1[y+i+1].append(x)
            except KeyError:
                path1[y+i+1] = [x]
        y += distance
    elif direction == "D":
        for i in range(distance):
            try:
                path1[y-i-1].append(x)
            except KeyError:
                path1[y-i-1] = [x]
        y -= distance
    else:
        print(f"Unexpected direction: {direction}")
        sys.exit()

x = 0
y = 0
intersections = []
for instruction in paths[1]:
    direction, distance = instruction[0], int(instruction[1:])
    if direction == "R":
        for i in range(distance):
            try:
                if x+i+1 in path1[y]:
                    intersections.append([y, x+i+1])
            except KeyError:
                pass
        x += distance
    elif direction == "L":
        for i in range(distance):
            try:
                if x-i-1 in path1[y]:
                    intersections.append([y, x-i-1])
            except KeyError:
                pass
        x -= distance
    elif direction == "U":
        for i in range(distance):
            try:
                if x in path1[y+i+1]:
                    intersections.append([y+i+1, x])
            except KeyError:
                pass
        y += distance
    elif direction == "D":
        for i in range(distance):
            try:
                if x in path1[y-i-1]:
                    intersections.append([y-i-1, x])
            except KeyError:
                pass
        y -= distance
    else:
        print(f"Unexpected direction: {direction}")
        sys.exit()

closest_distance = ()
for intersection in intersections:
    if intersection[0] < 0:
        intersection[0] = intersection[0] * -1
    if intersection[1] < 0:
        intersection[1] = intersection[1] * -1
    distance = intersection[0] + intersection[1]
    if closest_distance:
        if distance < closest_distance:
            closest_distance = distance
    else:
        closest_distance = distance

print(closest_distance)
