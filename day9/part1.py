from intcode_computer import Computer

with open("input.txt") as f:
    values = f.read()

values = values.rstrip().split(",")
values = [int(x) for x in values]

computer = Computer(values)
output = computer.run()
print(output)
