nums = input().split()
nums = [int(num) for num in nums]
nums.sort()
a, b, c = nums

order = input()
order = list(order)
final = []

for letter in order:
    if letter == "A":
        final.append(a)
    elif letter == "B":
        final.append(b)
    elif letter == "C":
        final.append(c)


ans = " ".join(map(str, final))
print(ans)
