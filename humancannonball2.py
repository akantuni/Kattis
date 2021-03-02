import math

n = int(input())

for i in range(n):
    params = input().split()
    v0 = float(params[0])
    theta = float(params[1])
    x1 = float(params[2])
    h1 = float(params[3])
    h2 = float(params[4])

    t = x1 / (v0 * math.cos(math.radians(theta)))
    y = (v0 * t * math.sin(math.radians(theta))) - (0.5 * 9.81 * (t ** 2))

    if h1 + 1 < y < h2 - 1:
        print("Safe")
    else:
        print("Not Safe")
