x = input()
basenumber = x.split()[0]
basenumber2 = x.split()[1]

number = basenumber[::-1]
number2 = basenumber2[::-1]

if number > number2:
    print(number)
else:
    print(number2)
