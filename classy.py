t = int(input())

for i in range(t):
    n = int(input())
    memo = {}
    for j in range(n):
        name, cls = input().split(" class")[0].split(": ")
        cls = (cls.split("-")[::-1] + ["middle"] * 10)[:10]
        memo.update({name: cls})

    points = {"upper": 3, "middle": 2, "lower": 1}
    totals = []

    for key, value in memo.items():
        totals.append(([points[identifier] for identifier in value], key))

    totals.sort(key=lambda x: x[1])
    totals.sort(key=lambda x: x[0], reverse=True)
    print("\n".join(item[1] for item in totals))
    print("=" * 30)
