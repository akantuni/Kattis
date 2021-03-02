n = int(input())

sec = 0
min = 0

for i in range(n):
    s = input()
    min += int(s.split()[0])
    sec += int(s.split()[1])

sl = sec / 60 / min

if sl > 1:
    print(sl)
else:
    print("measurement error")
