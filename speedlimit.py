distance = 0


def miles(w):
    time = 0
    dist = 0
    for i in range(w):
        if i == 0:
            x = input()
            speed = int(x.split()[0])
            hr = int(x.split()[1])
            time += hr
            dist += hr * speed
        else:
            x = input()
            speed = int(x.split()[0])
            hr = int(x.split()[1])
            hr = hr - time
            dist += hr * speed
            time += hr

    return dist


while True:
    z = input()
    if z == "-1":
        break
    elif len(z.split()) == 1:
        n = int(z)
        distance = miles(n)
        print(distance, "miles")
