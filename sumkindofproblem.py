t = int(input())

for i in range(t):
    k, n = list(map(int, input().split()))
    arr = [str(k)]
    arr.append(str(((1 + n) * n // 2)))
    arr.append(str(n ** 2))
    arr.append(str((2 + n * 2) * n // 2))

    print(" ".join(arr))
