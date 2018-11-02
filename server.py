n = input()
tasks = int(n.split()[0])
minutes = int(n.split()[1])
list = input()

flist = list.split()
total = 0
tasknum = 0

for e in flist:
    if total + int(e) > minutes:
        break
    else:
        total += int(e)
        tasknum += 1

print(tasknum)