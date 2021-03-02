def digit_sum(n):
    x = [int(i) for i in str(n)]
    return sum(x)


while True:
    n = int(input())
    nd = digit_sum(n)
    if n == 0:
        break
    p = 11
    while True:
        pd = digit_sum(p * n)
        if pd == nd:
            print(p)
            break
        p += 1
