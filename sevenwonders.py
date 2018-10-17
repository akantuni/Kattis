x = input()

nT = 0
nC = 0
nG = 0

xf = list(x)

for i in xf:
    if i == "T":
        nT += 1

for i in xf:
    if i == "G":
        nG += 1

for i in xf:
    if i == "C":
        nC += 1

points = nT ** 2 + nC ** 2 + nG ** 2

if "T" in xf and "G" in xf and "C" in xf:
    if min(nT, nG, nC) == 1:
        points += 7
    elif min(nT, nG, nC) > 1:
        points += (min(nT, nG, nC) * 7)

print(points)
