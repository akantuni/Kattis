import string

encrypted = input()
key = input()

alphabet = string.ascii_uppercase
final = ""

for i, letter in enumerate(key):
    idx = alphabet.index(letter)
    # new_letter = alphabet[(alphabet.index(encrypted[i]) + idx) % len(alphabet)]
    if i % 2 == 0:
        new_letter = alphabet[(alphabet.index(encrypted[i]) - idx) % len(alphabet)]
    else:
        new_letter = alphabet[(alphabet.index(encrypted[i]) + idx) % len(alphabet)]

    final += new_letter

print(final)
