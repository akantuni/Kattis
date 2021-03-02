s = input()

e = int(s.split(" ")[0])
f = int(s.split(" ")[1])
c = int(s.split(" ")[2])

t = e + f

ans = 0

while t // c != 0:
    ans += t // c
    t = t // c + t % c
print(ans)
