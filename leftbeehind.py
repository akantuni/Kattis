while True:
    n = input().split()
    sweet = int(n[0])
    sour = int(n[1])

    if sweet == 0 and sour == 0:
        break
    elif sweet + sour == 13:
        print("Never speak again.")
    elif sour > sweet:
        print("Left beehind.")
    elif sweet > sour:
        print("To the convention.")
    elif sweet == sour:
        print("Undecided.")
