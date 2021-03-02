n = int(input())

for i in range(n):
    stores = int(input())
    positions = list(map(int, input().split()))
    positions.sort()
    print(int(((positions[stores - 1] - positions[0]) / 2 * 4)))
