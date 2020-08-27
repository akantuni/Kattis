import string

alphabet = string.ascii_uppercase

encrypted = input()
half1 = encrypted[:int(len(encrypted) / 2)]
half2 = encrypted[int(len(encrypted) / 2):]

half1_final = ""
half2_final = ""
final = ""

rotate1 = 0
rotate2 = 0
for char in half1:
    rotate1 += alphabet.index(char)

for char in half2:
    rotate2 += alphabet.index(char)

for char in half1:
    rotate1 %= 26
    half1_final += alphabet[(alphabet.index(char) + rotate1) % 26]

for char in half2:
    rotate2 %= 26
    half2_final += alphabet[(alphabet.index(char) + rotate2) % 26]


for i, char in enumerate(half1_final):
    rotate = alphabet.index(half2_final[i]) % 26
    final += alphabet[(alphabet.index(char) + rotate) % 26]

print(final)