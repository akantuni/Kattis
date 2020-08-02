n = list(map(int, input().split()))
r = n[0]
c = n[1]
zr = n[2]
zc = n[3]

array = []
for i in range(r):
    temp = input()
    line = []
    for char in temp:
        line.append(char)
    array.append(line)
array2 = []
for line in array:
    mystr = ""
    for char in line:
        for i in range(zc):
            mystr += char
    for i in range(zr):
        array2.append(mystr)

for element in array2:
    print(element)
