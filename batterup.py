n = int(input())
s = input()
at_bat = s.split()
total = 0

while n > 0:
    for e in at_bat:
        if int(e) < 0:
            at_bat.remove(e)
    n -= 1

for e in at_bat:
    total += int(e)


print(total / len(at_bat))
