memo = [int(i) for i in input().split()]
final = [1, 2, 3, 4, 5]


while memo != final:
    if memo[0] > memo[1]:
        memo[0], memo[1] = memo[1], memo[0]
        for_print = (
            str(memo[0])
            + " "
            + str(memo[1])
            + " "
            + str(memo[2])
            + " "
            + str(memo[3])
            + " "
            + str(memo[4])
        )
        print(for_print)
    if memo[1] > memo[2]:
        memo[1], memo[2] = memo[2], memo[1]
        for_print = (
            str(memo[0])
            + " "
            + str(memo[1])
            + " "
            + str(memo[2])
            + " "
            + str(memo[3])
            + " "
            + str(memo[4])
        )
        print(for_print)
    if memo[2] > memo[3]:
        memo[2], memo[3] = memo[3], memo[2]
        for_print = (
            str(memo[0])
            + " "
            + str(memo[1])
            + " "
            + str(memo[2])
            + " "
            + str(memo[3])
            + " "
            + str(memo[4])
        )
        print(for_print)
    if memo[3] > memo[4]:
        memo[3], memo[4] = memo[4], memo[3]
        for_print = (
            str(memo[0])
            + " "
            + str(memo[1])
            + " "
            + str(memo[2])
            + " "
            + str(memo[3])
            + " "
            + str(memo[4])
        )
        print(for_print)
