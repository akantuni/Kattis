n = int(input())

for i in range(n):
    num_digits = list(map(int, input()))[::-1]
    final = []
    for i, digit in enumerate(num_digits):
        if i % 2 == 0:
            final.append(digit)
        else:
            digit *= 2
            if len(str(digit)) > 1:
                digit = sum(map(int, list(str(digit))))
            final.append(digit)

    if sum(final) % 10 == 0:
        print("PASS")
    else:
        print("FAIL")