from math import log

nf = input()
lnf = len(nf)

if lnf < 4:
    i = 2
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
