s = input()
limit = int(s.split()[0])
n = int(s.split()[1])
total = 0
notall = 0

for i in range(n):
    line = input()
    action = line.split()[0]
    people = int(line.split()[1])
    if action == "enter":
        if total + people > limit:
            notall += 1
        else:
            total += people
    else:
        total -= people

print(notall)
