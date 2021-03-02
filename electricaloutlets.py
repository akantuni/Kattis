t = int(input())

for l in range(t):
    ls = list(map(int, input().split()))[1:]
    print(1 + sum(ls) - len(ls))
