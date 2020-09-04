r, n = list(map(int, input().split()))

memo = set()

for i in range(n):
    room_number = int(input())
    memo.add(room_number)

if len(memo) == r:
    print("too late")
else:
    for i in range(1, r + 1):
        if i not in memo:
            print(i)
            break
