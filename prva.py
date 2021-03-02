r, c = [int(i) for i in input().split()]
words = []
g = []

for i in range(r):
    row = input()
    g.append(row)

for i in range(r):
    for j in range(c):
        if g[i][j] == "#":
            continue
        if j == 0 or g[i][j - 1] == "#":
            word = ""
            for k in range(j, c):
                if g[i][k] != "#":
                    word += g[i][k]
                else:
                    break
            if len(word) > 1:
                words.append(word)
        if i == 0 or g[i - 1][j] == "#":
            word = ""
            for k in range(i, r):
                if g[k][j] != "#":
                    word += g[k][j]
                else:
                    break
            if len(word) > 1:
                words.append(word)

words.sort()
print(words[0])


# if i != 0 and j != 0 and (g[i - 1][j] == "#" or g[i][j - 1] == "#"):
