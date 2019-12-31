import copy

with open("input.txt") as f:
    data = f.readlines()

data = [x.rstrip().split(")") for x in data]

orbits = dict()
for line in data:
    orbits[line[1]] = line[0]

counter = 0
for i in orbits.keys():
    j = copy.deepcopy(i)
    while j in orbits.keys():
        j = orbits[j]
        counter += 1

print(counter)
