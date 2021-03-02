n = int(input())

days = set()

for i in range(n):
    dates = list(map(int, input().split()))
    for i in range(dates[0], dates[1] + 1):
        days.add(i)

print(len(days))
