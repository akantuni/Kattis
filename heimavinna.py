ranges = input().split(";")

total = 0
for item in ranges:
    item = item.split("-")
    if len(item) == 1:
        total += 1
    else:
        total += len(range(int(item[0]), int(item[1]) + 1))

print(total)
