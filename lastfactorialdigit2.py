t = int(input())
memo = [1, 1, 2, 6, 4]

for i in range(t):
    n = int(input())
    if n < 5:
        print(memo[n])
    else:
        print(0)
