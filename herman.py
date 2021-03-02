from math import sqrt, pi

radius = int(input())

euclidian_area = pi * radius ** 2
taxicab_area = (radius * sqrt(2)) ** 2

print(euclidian_area)
print(taxicab_area)
