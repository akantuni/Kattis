y, x = input().split()

vowels_no_e = ["a", "i", "o", "u"]

if (y[-2] + y[-1]) == "ex":
    print(y + x)
elif y[-1] == "e":
    print(y + "x" + x)
elif y[-1] in vowels_no_e:
    print(y[:-1] + "ex" + x)
else:
    print(y + "ex" + x)
