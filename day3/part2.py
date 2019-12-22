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
intersections = dict()
path_sum = 0
for instruction in paths[1]:
    direction, distance = instruction[0], int(instruction[1:])
    if direction == "R":
        for i in range(distance):
            try:
                if x+i+1 in path1[y]:
                    if (y, x+i+1) not in intersections.keys():
                        intersections[(y, x+i+1)] = path_sum + i + 1
            except KeyError:
                pass
        x += distance
    elif direction == "L":
        for i in range(distance):
            try:
                if x-i-1 in path1[y]:
                    if (y, x-i-1) not in intersections.keys():
                        intersections[(y, x-i-1)] = path_sum + i + 1
            except KeyError:
                pass
        x -= distance
    elif direction == "U":
        for i in range(distance):
            try:
                if x in path1[y+i+1]:
                    if (y+i+1, x) not in intersections.keys():
                        intersections[(y+i+1, x)] = path_sum + i + 1
            except KeyError:
                pass
        y += distance
    elif direction == "D":
        for i in range(distance):
            try:
                if x in path1[y-i-1]:
                    intersections[(y-i-1, x)] = path_sum + i + 1
            except KeyError:
                pass
        y -= distance
    else:
        print(f"Unexpected direction: {direction}")
        sys.exit()
    path_sum += distance

x = 0
y = 0
path_sum = 0
for instruction in paths[0]:
    print(instruction)
    direction, distance = instruction[0], int(instruction[1:])
    if direction == "R":
        for i in range(distance):
            if (y, x+i+1) in intersections.keys():
                intersections[(y, x+i+1)] += path_sum + i + 1
        x += distance
    elif direction == "L":
        for i in range(distance):
            if (y, x-i-1) in intersections.keys():
                intersections[(y, x-i-1)] += path_sum + i + 1
        x -= distance
    elif direction == "U":
        for i in range(distance):
            if (y+i+1, x) in intersections.keys():
                intersections[(y+i+1, x)] += path_sum + i + 1
        y += distance
    elif direction == "D":
        for i in range(distance):
            if (y-i-1, x) in intersections.keys():
                intersections[(y-i-1, x)] += path_sum + i + 1
        y -= distance
    else:
        print(f"Unexpected direction: {direction}")
        sys.exit()
    path_sum += distance

fewest_steps = ()
for intersection in intersections:
    print(intersection, intersections[intersection])
    num_steps = intersections[intersection]
    if fewest_steps:
        if num_steps < fewest_steps:
            fewest_steps = num_steps
    else:
        fewest_steps = num_steps

print(fewest_steps)
