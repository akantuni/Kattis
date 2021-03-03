t = int(input())

nums = []

for i in range(t):
    nums.append(int(input()))

nums = nums[::-1]

for num in nums:
    print(num)
