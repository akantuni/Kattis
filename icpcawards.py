n = int(input())
collages = []

for i in range(n):
    s = input()
    collage = s.split()[0]
    if collage in collages:
        continue
    elif len(collages) != 12:
        collages.append(collage)
        print(s)
