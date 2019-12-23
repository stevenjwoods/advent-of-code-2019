def identical_adjacent_digits(password):
    for j in range(len(password)-1):
        if password[j] == password[j + 1]:
            return True


def digits_never_decrease(password):
    for j in range(len(password)-1):
        if int(password[j]) <= int(password[j+1]):
            continue
        else:
            return False
    return True


def exact_double(password):
    for j in range(len(password)-1):
        try:
            if password[j] == password[j+1] and password[j] not in [password[j-1], password[j+2]]:
                return True
        except IndexError:
            if j == 0 and password[j] == password[j+1] and password[j] != password[j+2]:
                return True
            elif j == len(password) - 2 and password[j] == password[j+1] and password[j] != password[j-1]:
                return True
            else:
                return False


with open("input.txt") as f:
    number_range = f.readline()

start, stop = number_range.rstrip().split("-")

num_passwords = 0
i = int(start)

while i <= int(stop):
    if identical_adjacent_digits(str(i)) and digits_never_decrease(str(i)):
        if exact_double(str(i)):
            num_passwords += 1
    i += 1

print(num_passwords)