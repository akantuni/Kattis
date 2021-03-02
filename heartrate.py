n = int(input())

for i in range(n):
    case = input().split()
    b = float(case[0])
    p = float(case[1])

    bpm = round(60 * b / p, 4)
    minabpm = round(60 * (b - 1) / p, 4)
    maxabpm = round(60 * (b + 1) / p, 4)

    print(minabpm, bpm, maxabpm)
