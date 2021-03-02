n = input()
memo = [int(i) for i in n]
x = int(n)

if x % sum(memo) == 0:
    print(x)
else:
    while True:
        x += 1
        memo = [int(i) for i in str(x)]
        if x % sum(memo) == 0:
            print(x)
            break
