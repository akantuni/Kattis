n, m = list(map(int, input().split()))

lists = []
for i in range(n):
    lists.append(input().split())

items = sorted(set.intersection(*map(set, lists)))

print(len(items))
for item in items:
    print(item)
