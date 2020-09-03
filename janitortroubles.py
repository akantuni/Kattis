from math import sqrt

x = list(map(int, input().split()))

s = sum(x) / 2

ans = sqrt((s - x[0]) * (s - x[1]) * (s - x[2]) * (s - x[3]))

print(ans)
