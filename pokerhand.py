n = [list(val)[0] for val in input().split()]


mx = 0

for letter in n:
    if n.count(letter) > mx:
        mx = n.count(letter)

print(mx)