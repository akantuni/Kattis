line = input()

x = int(line.split()[0])
y = int(line.split()[1])

if x == 0 and y == 0:
    print("Not a moose")
elif x != y:
    ans = int(max(x, y)) + int(max(x, y))
    print("Odd", int(ans))
elif x == y:
    print("Even", x + y)
