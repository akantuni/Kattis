n = int(input())

def ssd(y):
    sum = 0
    for number in y[2]:
        counter = y[2].index(number)
        sum += int(number) * (int(y[1]) ** counter)
    return sum

def ssd2(y):
    sum = 0
    for number in str(y):
        # print(number)
        sum += int(number) ** 2
    return sum

for i in range(n):
    x = input().split()

    temp = ssd(x)
    print(temp)
    print(ssd2(temp))
