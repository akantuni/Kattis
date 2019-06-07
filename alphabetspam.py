n = input()

space = 0
lower = 0
upper = 0
symbols = 0
length = len(n)

for char in n:
    if char == "_":
        space += 1
    elif char.islower():
        lower += 1
    elif char.isupper():
        upper += 1
    else:
        symbols += 1

print(space / length)
print(lower / length)
print(upper / length)
print(symbols / length)