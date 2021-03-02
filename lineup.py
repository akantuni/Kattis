n = int(input())
original = []


for i in range(n):
    name = input()
    original.append(name)

mutated = sorted(original)
reverse_mutated = mutated[::-1]

if mutated == original:
    print("INCREASING")
elif reverse_mutated == original:
    print("DECREASING")
else:
    print("NEITHER")
