x = int(input())

days = 1
printers = 1

while printers < x:
    days += 1
    printers *= 2

print(days)