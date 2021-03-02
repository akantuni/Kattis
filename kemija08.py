s = input()

vowels = ["a", "e", "i", "o", "u"]

i = 0
while i < len(s):
    if s[i] in vowels:
        s = s[0 : i + 1] + s[i + 3 : len(s)]
    i += 1
print(s)
