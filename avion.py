arr = []
for i in range(5):
    string = input()
    counter = -1
    for letter in string:
        counter += 1
        if (
            counter + 2 < len(string)
            and letter == "F"
            and string[counter + 1] == "B"
            and string[counter + 2] == "I"
        ):
            arr.append(str(i + 1))

if len(arr) > 0:
    print(" ".join(arr))
else:
    print("HE GOT AWAY!")
