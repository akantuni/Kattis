n = int(input())
answers = input()

adrian = "ABC"
bruno = "BABC"
goran = "CCAABB"

memo = {"Adrian": 0, "Bruno": 0, "Goran": 0}

for i in range(n):
    if answers[i] == adrian[i % len(adrian)]:
        memo["Adrian"] += 1
    if answers[i] == bruno[i % len(bruno)]:
        memo["Bruno"] += 1
    if answers[i] == goran[i % len(goran)]:
        memo["Goran"] += 1

m = max(memo.values())

print(m)

for name, score in memo.items():
    if score == m:
        print(name)
