names = []

while True:
    try:
        name = input().split()[::-1]
        names.append(name)
    except EOFError:
        break

duplicate_names = []
names.sort()
memo = {}

for last_name, first_name in names:
    memo[first_name] = memo.get(first_name, 0) + 1

for last_name, first_name in names:
    if memo.get(first_name) > 1:
        print(first_name, last_name)
    else:
        print(first_name)
