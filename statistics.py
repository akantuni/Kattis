case = 0
while True:
    try:
        case += 1
        x = [int(i) for i in input().split()[1::]]
        minx = min(x)
        maxx = max(x)
        print("Case", str(case) + ":", minx, maxx, maxx - minx)
    except EOFError:
        break
