s = input()
type = s.split()[0]
text = s.split()[1]
num = "123456789"

def encode(text):
    mystr = ""
    total = 0
    for letter in text:
        if len(mystr) != 0 and letter == mystr[len(mystr) - 1]:
            total += 1
        elif total == 0:
            mystr += letter
            total += 1
        else:
            mystr += str(total)
            mystr += letter
            total = 1
    return mystr + str(total)


def decode(text):
    mystr = ""
    for i in text:
        if i in num:
            for e in range(int(i) - 1):
                mystr += mystr[len(mystr) - 1]
        else:
            mystr += i
    return mystr


if type == "E":
    print(encode(text))
elif type == "D":
    print(decode(text))
