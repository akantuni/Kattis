n = int(input())

counter = 0

for i in range(n):
    color = input().lower()
    if "pink" in color or "rose" in color:
        counter += 1

if counter == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(counter)
