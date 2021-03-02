n = int(input())

memo = {}

for i in range(n):
    cin = input().split()

    color = None
    radius = None

    if cin[0].isdigit():
        radius = int(cin[0]) // 2
        color = cin[1]
    else:
        color = cin[0]
        radius = int(cin[1])

    memo.update({radius: color})

for key in sorted(list(memo.keys())):
    print(memo.get(key))
