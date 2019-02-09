x = input()
list = input().split()
list2 = []
lowest = int(list[0])

for i in list:
    i = int(i)
    list2.append(i)


for e in list2:
    if lowest > e:
        lowest = e

ind = list.index(str(lowest))

print(ind)