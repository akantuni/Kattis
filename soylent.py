import math
n = int(input())

for i in range(n):
    calories = int(input())
    print(math.ceil(calories / 400))