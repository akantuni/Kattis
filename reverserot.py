

while True:
    line = input().upper()
    guide = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    split = line.split(" ")

    num = int(split[0])
    if num == 0:
        break

    s = split[1]
    revs = s[::-1]

    fs = ""
    for char in revs:
        fsnum = (guide.index(char) + num) % len(guide)
        fs += guide[fsnum]

    print(fs)
