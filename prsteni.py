from math import gcd

n = int(input())
rings = [int(i) for i in input().split()]
first, *rest = rings

for ring in rest:
    numerator = first // gcd(first, ring)
    denominator = ring // gcd(first, ring)
    print("{}/{}".format(numerator, denominator))
 