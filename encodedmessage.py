import math

a = int(input())
for num in range(a):
    n = input()
    x = int(math.sqrt(len(n)))

    s = [n[i : i + x] for i in range(0, len(n), x)]
    mystr = ""

    def decrypt(y):
        global mystr
        for i, e in enumerate(y):
            mystr += e[len(e) - 1]
            y[i] = e[0 : (len(e) - 1)]
        if len(y[0]) > 0:
            decrypt(y)

    decrypt(s)
    print(mystr)
