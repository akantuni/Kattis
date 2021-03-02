n = int(input())

n = bin(n)[2:]

x = n[::-1]

print(int("0b" + x, 2))
