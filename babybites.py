n = int(input())
numbers = input()
makes_sense = True

for index, number in enumerate(numbers.split()):
    if number != "mumble" and int(number) != (index + 1):
        makes_sense = False
        break

if makes_sense:
    print("makes sense")
else:
    print("something is fishy")
