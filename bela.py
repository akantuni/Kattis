s = input()
n = int(s.split()[0])
b = s.split()[1]
total = 0

dominant = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
not_dominant = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}

for i in range(4 * n):
    card = input()
    if card[1] == b:
        total += dominant.get(card[0])
    else:
        total += not_dominant.get(card[0])
print(total)