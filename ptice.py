n = int(input())
answers = input()

adrian = ["A", "B", "C"]
bruno = ["B", "A", "B", "C"]
gordan = ["C", "C", "A", "A", "B", "B"]

correct_a = 0
correct_b = 0
correct_g = 0
for i, char in enumerate(answers):
    if adrian[i % 3] == char:
        correct_a += 1
    if bruno[i % 4] == char:
        correct_b += 1
    if gordan[i % 6] == char:
        correct_g += 1

m = max(correct_a, correct_b, correct_g)

print(m)

if correct_a == m:
    print("Adrian")
if correct_b == m:
    print("Bruno")
if correct_g == m:
    print("Gordan")
