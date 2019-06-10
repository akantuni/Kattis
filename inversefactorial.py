from math import log

nf = input()
lnf = len(nf)

if nf == "1":
    print(1)
elif lnf < 4:
    i = 1
    total = 1
    while total != int(nf):
        total *= i
        i += 1

    print(i - 1)
else:
    i = 1
    total = 0

    while total < lnf:
        total += log(i, 10)
        i += 1

    print(i - 2)
