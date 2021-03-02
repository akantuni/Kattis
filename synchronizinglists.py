n = float("inf")
while n > 0:
    n = int(input())
    fixed = []
    unordered = []
    sorted_fixed = []
    sorted_unordered = []
    memo = {}
    final = []
    for i in range(n):
        fixed.append(int(input()))
    for i in range(n):
        unordered.append(int(input()))

    sorted_fixed = sorted(fixed)
    sorted_unordered = sorted(unordered)

    for i in range(len(fixed)):
        memo.update({sorted_fixed[i]: sorted_unordered[i]})

    for number in fixed:
        final.append(str(memo.get(number)))

    print("\n".join(final))
