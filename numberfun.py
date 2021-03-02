n = int(input())

for i in range(n):
    nums = input().split()
    nums = [int(num) for num in nums]
    a, b, c = nums

    if a + b == c:
        print("Possible")
    elif a * b == c:
        print("Possible")
    elif a - b == c or b - a == c:
        print("Possible")
    elif a == c * b or b == c * a:
        print("Possible")
    else:
        print("Impossible")

a, b = b, a
