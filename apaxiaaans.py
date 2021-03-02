s = input()
mystr = ""

for i in s:
    if len(mystr) == 0:
        mystr += i
    elif i == mystr[len(mystr) - 1]:
        continue
    else:
        mystr += i

print(mystr)
