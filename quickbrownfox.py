alphabet = "abcdefghijklmnopqrstuvwxyz"
n = int(input())

for e in range(n):
    s = input()
    s = s.lower()
    s = s.replace(" ", "")
    missing = ""
    for e in alphabet:
        if e not in s:
            missing += e

    if len(missing) > 0:
        print("missing", missing)
    else:
        print("pangram")
