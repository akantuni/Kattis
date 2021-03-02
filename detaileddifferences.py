n = int(input())
mystr = ""

for i in range(n):
    mystr = ""
    s1 = input()
    s2 = input()
    x = s1
    y = s2

    for e in range(len(s1)):
        if x[0] == y[0]:
            mystr += "."
        else:
            mystr += "*"

        x = x[1:]
        y = y[1:]

    print(s1)
    print(s2)
    print(mystr)
    print()
