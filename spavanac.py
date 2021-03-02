time = input()

h = int(time.split()[0])
m = int(time.split()[1])

m -= 45

if m < 0:
    h -= 1
    m += 60

if h < 0:
    h += 24

print(h, m)
