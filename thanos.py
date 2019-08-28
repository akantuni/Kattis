n = int(input())

for i in range(n):
    case = input().split()
    p = int(case[0])
    r = int(case[1])
    f = int(case[2])
    years = 0

    while p <= f:
        years += 1
        p *= r

    print(years)