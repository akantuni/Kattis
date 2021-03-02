l = int(input())
d = int(input())
x = int(input())


def digits(z):
    s = 0
    while z > 0:
        s += z % 10
        z //= 10
    return s


n = l
for n in range(l, d + 1):
    if digits(n) == x:
        break

m = d
for m in range(d, l - 1, -1):
    if digits(m) == x:
        break

print(n)
print(m)
