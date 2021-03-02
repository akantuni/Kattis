n = int(input())

for e in range(n):
    l = input()
    if "+" not in l:
        print("skipped")
    else:
        one = int(l.split("+")[0])
        two = int(l.split("+")[1])
        print(one + two)
