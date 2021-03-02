s = int(input())

print(str(s) + ":")

for k in range(2, s):
    total = 0
    i = 0

    while total < s:
        if i % 2 == 0:
            total += k
        else:
            total += k - 1
        i += 1

    if total == s:
        print(str(k) + "," + str(k - 1))

    if s % k == 0:
        print(str(k) + "," + str(k))
