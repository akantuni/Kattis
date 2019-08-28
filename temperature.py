details = [int(i) for i in input().split()]
x, y = details
try:
    if y == 0 and x == 0:
        print("ALL GOOD")
    elif y == 0 and x != 0:
        print("IMPOSSIBLE")
    else:
        print((x/(1-y)))
except ZeroDivisionError:
    if x == 0:
        print("ALL GOOD")
    else:
        print("IMPOSSIBLE")

