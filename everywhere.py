n = int(input())

list = []

for i in range(n):
    m = int(input())
    for i in range(m):
        city = input()
        if len(city) > 0 and city not in list:
            list.append(city)
        else:
            continue
    print(len(list))
    list = []
