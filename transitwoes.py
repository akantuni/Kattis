import math

s, t, n = list(map(int, input().split()))
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

total = s
for i in range(n):
    total += d[i]
    diff = math.ceil(total / c[i]) * c[i] - total
    total += diff
    total += b[i]

total += d[-1]

if total <= t:
    print("yes")
else:
    print("no")
