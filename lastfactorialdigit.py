t = int(input())
total = 1

for i in range(t):
    total = 1
    n = int(input())
    for e in range(1, n + 1):
        total *= e
    print(total % 10)
