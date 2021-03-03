n = int(input())

answers = []
for i in range(n):
    answers.append(input())

total = 0
for i in range(len(answers) - 1):
    if answers[i] == answers[i + 1]:
        total += 1

print(total)
