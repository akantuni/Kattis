hex_chars = "abcdef0123456789"
x = 1

while x != "":
    try:
        str = input()

        hexes = []

        for i, char in enumerate(str):
            hex = ""

            if char == "0" and (i + 1) != len(str):
                if str[i + 1].lower() == "x":
                    potential_hex = str[i + 2 : i + 10]
                    for character in potential_hex:
                        if character.lower() in hex_chars:
                            hex += character
                        else:
                            break

                    if len(hex) > 0:
                        hex = "0" + str[i + 1] + hex
                        hexes.append(hex)
                        hex = ""

        for hex_num in hexes:
            print(hex_num, int(hex_num, 16))

    except EOFError:
        break
