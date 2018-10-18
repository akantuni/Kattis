import math
n = input()

h = int(n.split()[0])
v = int(n.split()[1])

radians = 0.0174533 * v

x = math.sin(radians)

print(math.ceil(h / x))
