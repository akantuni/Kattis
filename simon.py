n = input()
for e in range(int(n)):
    str = ""
    line = input()
    if line.startswith("simon says"):
        arraystr = line.split(" ")[2:]
        for word in arraystr:
            str += (word + " ")
    if len(str) > 0:
        print(str[:-1] + '\n')
