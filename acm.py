submissions = []
min = 0
probs = 0

while True:
    x = input().split()
    if x == ["-1"]:
        break
    submissions.append(x)

problems = {}

for i in submissions:
    problems.update({i[1]: False})

for i in submissions:
    if i[2] == "right":
        problems[i[1]] = True
        min += int(i[0])
        probs += 1

for i in submissions:
    if i[2] == "wrong" and problems[i[1]] == True:
        min += 20

print(probs, min)
