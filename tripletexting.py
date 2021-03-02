string = input()

memo = [
    string[0 : (len(string) // 3)],
    string[len(string) // 3 : ((len(string) // 3) * 2)],
    string[((len(string) // 3) * 2) : len(string)],
]

freq = 0
most = 0

for item in memo:
    x = memo.count(item)
    if x > most:
        most = x
        freq = item

print(freq)
