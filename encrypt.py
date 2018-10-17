alphabet = "abcdefghijklmnopqrstuvwxyz"

letternum = {"a": 5, "b": 6, "c": 8, "d": 3, "e": 12, "f": 4, "g": 7, "h": 15, "i": 1, "j": 0, "k": 9, "l": 2, "m": 7,
             "n": 11, "o": 10, "p": 4, "q": 2, "r": 8, "s": 6, "t": 5, "u": 3, "v": 3, "w": 2, "x": 1, "y": 0,
             "z": 24, }

restart = True

while restart:
    restart = False
    prompt = input("Please type '1' if you want to encrypt and '2' if you want to decrypt: ")

    if prompt == "1":
        inn = input("Please enter your message: ").lower()

        mystr = ""

        for letter in inn:
            le = letternum.get(letter)
            ind = mystr.find(letter) + le
            mystr += alphabet[ind]

        print(mystr)

# decrypt not working, index does not move back same number as in encrypt
    elif prompt == "2":
        inn2 = input("Please enter the message you want to decrypt: ").lower()

        mystr2 = ""

        for letter2 in inn2:
            le2 = letternum.get(letter2)
            ind2 = mystr2.find(letter2) - le2
            mystr2 += alphabet[ind2]

        print(mystr2)

    else:
        break


    ans = input("If you want to encrypt/decrypt another message please type 'restart', or if you are done please type 'done': ")

    if ans == "done":
        break

    elif ans == "restart":
        restart = True



