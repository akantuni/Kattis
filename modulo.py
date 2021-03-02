unique = []

for i in range(10):
    n = int(input())
    if n % 42 not in unique:
        unique.append(n % 42)

print(len(unique))
