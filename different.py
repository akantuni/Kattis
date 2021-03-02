import sys

for line in sys.stdin:
    x = int(line.split()[0])
    y = int(line.split()[1])

    print(abs(x - y))
