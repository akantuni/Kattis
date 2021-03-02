x = input().split()

n = int(x[0])
h = int(x[1])
v = int(x[2])

sq1 = v * h * 4
sq2 = (n - v) * h * 4
sq3 = (n - h) * (n - v) * 4
sq4 = (n - h) * v * 4

final = [sq1, sq2, sq3, sq4]
final.sort()

print(final[3])
