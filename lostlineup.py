n = int(input())

lineup = list(map(int, input().split()))
sorted_lineup = sorted(lineup)

final = ["1"]

for item in sorted_lineup:
    final.append(str(lineup.index(item) + 2))

print(" ".join(final))
