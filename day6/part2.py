class Node:

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def __str__(self):
        return self.name


with open("input.txt") as f:
    data = f.readlines()

data = [x.rstrip().split(")") for x in data]
nodes = dict()
for line in data:
    nodes[line[0]] = Node(line[0])
    nodes[line[1]] = Node(line[1])

for line in data:
    nodes[line[0]].children.append(nodes[line[1]])
    nodes[line[1]].parent = nodes[line[0]]

for key, node in nodes.items():
    if node.name == "YOU":
        you = node
    if node.name == "SAN":
        santa = node

santa_path = []
destination_node = santa.parent

while santa.parent.name != "COM":
    santa_path.append(santa.parent.name)
    santa.parent = santa.parent.parent
santa_path.append(santa.parent.name)

santa.parent = destination_node

counter = 0
while you.parent.name not in santa_path:  # Note 'YOU' doesn't get removed from children...
    you.parent = you.parent.parent
    counter += 1

while you.parent != santa.parent:
    if len(you.parent.children) == 1:
        you.parent = you.parent.children[0]
    else:
        for child in you.parent.children:
            if child.name in santa_path:
                you.parent = child
    counter += 1

print(counter)

