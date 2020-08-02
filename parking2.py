n = int(input())

for i in range(n):
    numstores = int(input())
    coordinates = list(map(int, input().split()))
    coordinates.sort()
    sum = 0
    for i in coordinates:
        while coordinates.index(i) + 1 < numstores:
            sum += 2 * abs((i - coordinates[coordinates.index(i) + 1]))
            break
    print(sum)
