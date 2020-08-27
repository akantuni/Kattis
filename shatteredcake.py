width = int(input())
shapes = int(input())

area = 0
for i in range(shapes):
    dimentions = input().split()
    area += int(dimentions[0]) * int(dimentions[1])

print(int(area / width))