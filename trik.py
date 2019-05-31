operations = input()

a = 1
b = 0
c = 0

for op in operations:
    if op is "A":
        a, b = b, a
    elif op is "B":
        b, c = c, b
    else:
        a, c = c, a

if a is 1:
    print(1)
elif b is 1:
    print(2)
else:
    print(3)
