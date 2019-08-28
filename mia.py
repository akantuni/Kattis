while True:
    rolls = input().split()
    if rolls == ['0', '0', '0', '0']:
        break
    p1 = int(str(max(int(rolls[0]), int(rolls[1]))) + str(min(int(rolls[0]), int(rolls[1]))))
    p2 = int(str(max(int(rolls[2]), int(rolls[3]))) + str(min(int(rolls[2]), int(rolls[3]))))

    if p1 == 12 or p1 == 21:
        if p2 == 12 or p2 == 21:
            print("Tie.")
        else:
            print("Player 1 wins.")
    elif p2 == 12 or p2 == 21:
        print("Player 2 wins.")
    elif str(p1)[0] == str(p1)[1]:
        if str(p2)[0] == str(p2)[1]:
            if p1 > p2:
                print("Player 1 wins.")
            elif p2 > p1:
                print("Player 2 wins.")
            else:
                print("Tie.")
        else:
            print("Player 1 wins.")
    elif str(p2)[0] == str(p2)[1]:
        print("Player 2 wins.")
    else:
        if p1 > p2:
            print("Player 1 wins.")
        elif p2 > p1:
            print("Player 2 wins.")
        else:
            print("Tie.")
