n = input()

words = n.split("-")
str = ""

for word in words:
    str += word[0]

print(str)
