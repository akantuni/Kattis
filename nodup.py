s = input()
words = s.split(" ")
nodup = []

for word in words:
    if word not in nodup:
        nodup.append(word)
    else:
        print("no")
        break

if len(nodup) == len(words):
    print("yes")
