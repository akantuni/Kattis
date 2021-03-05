while True:
    x, y, z = sorted(list(map(int, input().split())))

    if x == 0 and y == 0 and z == 0:
        break
    elif x ** 2 + y ** 2 == z ** 2:
        print("right")
    else:
        print("wrong")
