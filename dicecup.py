n = input().split()

d1 = int(n[0])
d2 = int(n[1])

memo = {}
greatest = []
mx = 1

for i in range(1, d1 + 1):
    for j in range(1, d2 + 1):
        if j + i not in memo:
            memo[j + i] = 1
        else:
            memo[j + i] += 1
            mx = max(mx, memo[j + i])

for key in memo:
    if memo[key] == mx:
        greatest.append(key)

greatest.sort()

for val in greatest:
    print(val)
