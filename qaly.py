n = int(input())
total = 0

for i in range(n):
    s = input()
    x = float(s.split()[0])
    y = float(s.split()[1])
    total += x * y

print("{:.3f}".format(total))
