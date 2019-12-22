with open('input.txt') as f:
    modules = f.readlines()


def calculate_fuel(mass):
    fuel = 0
    while mass > 0:
        mass = int(mass/3) - 2
        if mass > 0:
            fuel += mass
    return fuel


fuel_requirement = sum([calculate_fuel(int(mass.rstrip())) for mass in modules])
print(fuel_requirement)
