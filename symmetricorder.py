loop = 0
while True:
    loop += 1
    names = []
    memo1 = []
    memo2 = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        name = input()
        names.append(name)
    for item in names:
        if names.index(item) % 2 == 0:
            memo1.append(item)
        else:
            memo2.append(item)
    final = memo1 + memo2[::-1]
    print("SET", loop)
    for i in final:
        print(i)