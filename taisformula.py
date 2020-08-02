n = int(input())
coordinates = []

for i in range(n):
    point = input()
    coordinates.append(list(map(float, point.split())))

x = 0
areas = []
for i in range(len(coordinates) - 1):
    area = ((coordinates[x][1] + coordinates[x + 1][1]) / 2) * (coordinates[x + 1][0] - coordinates[x][0]) / 1000
    areas.append(area)
    x += 1

sum = 0
for area in areas:
    sum += area

if sum == int(sum):
    print(int(sum))
else:
    print(sum)