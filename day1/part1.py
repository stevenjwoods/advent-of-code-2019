with open('input.txt') as f:
    modules = f.readlines()


def calculate_fuel(mass):
    return int(mass/3) - 2


fuel_requirement = sum([calculate_fuel(int(mass.rstrip())) for mass in modules])
print(fuel_requirement)
