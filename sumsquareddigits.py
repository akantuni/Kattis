def convert_to_base(num, base):
    memo = []
    remainder = None
    while num > 0:
        remainder = num % base
        num //= base
        memo.append(remainder)

    return memo

n = int(input())

for i in range(n):
    ssd = 0
    x = list(map(int, input().split()))
    k = x[0]
    b = x[1]
    num = x[2]

    # print(num, convert_to_base(num, b))
    for digit in convert_to_base(num, b):
        ssd += int(digit) ** 2

    print(k, ssd)
