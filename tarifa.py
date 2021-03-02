x = int(input())
n = int(input())

ans = 0
while n > 0:
    p = int(input())
    ans = ans + (x - p)
    n = n - 1

ans = ans + x

print(ans)
