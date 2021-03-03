t = int(input())

locs = []

for i in range(t):
    locs.append(tuple(map(int, input().split())))

speed = 0

for i in range(1, len(locs)):
    current = (locs[i][1] - locs[i - 1][1]) / (locs[i][0] - locs[i - 1][0])
    if current > speed:
        speed = current

print(int(speed))

