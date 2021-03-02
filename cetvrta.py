a = input().split()
b = input().split()
c = input().split()

x = []
y = []

x.append(a[0])
x.append(b[0])
x.append(c[0])

y.append(a[1])
y.append(b[1])
y.append(c[1])


def remove(n):
    semi = []
    dup = []
    for num in n:
        if num not in semi:
            semi.append(num)
        else:
            dup.append(num)
    for num in semi:
        if num not in dup:
            return num


print(remove(x), remove(y))
