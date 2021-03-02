n = int(input())

for i in range(n):
    k, days = list(map(int, input().split()))
    total = days
    for i in range(1, days + 1):
        total += i
    print(k, total)
