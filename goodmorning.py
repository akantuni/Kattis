cases = int(input())

correspondances = {
    "1": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    "2": ["2", "3", "5", "6", "8", "9", "0"],
    "3": ["3", "6", "9"],
    "4": ["4", "5", "6", "7", "8", "9", "0"],
    "5": ["5", "6", "8", "9", "0"],
    "6": ["6", "9"],
    "7": ["7", "8", "9", "0"],
    "8": ["8", "9", "0"],
    "9": ["9"],
    "0": ["0"]
}


def is_possible(k):
    possible = True
    for i, digit in enumerate(k):
        try:
            next_digit = k[i + 1]
            if next_digit not in correspondances.get(digit):
                possible = False
                break
        except:
            continue

    return possible


for i in range(cases):
    x = int(input())

    if is_possible(str(x)):
        print(x)
    else:
        y = x + 1
        z = x - 1
        while True:
            if is_possible(str(y)):
                print(y)
                break
            elif is_possible(str(z)):
                print(z)
                break
            else:
                y += 1
                z -= 1
