n = int(input())

money = [int(i) for i in input().split()]

total = 0

for i in money:
    if i < 0:
        total += abs(i)

print(total)