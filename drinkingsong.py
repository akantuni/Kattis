n = int(input())
bev = input().lower()

for i in reversed(range(1, n + 1)):
    if i == 1:
        print(
            f"1 bottle of {bev} on the wall, 1 bottle of {bev}.\nTake it down, pass it around, no more bottles of {bev}."
        )
    elif i == 2:
        print(
            f"2 bottles of {bev} on the wall, 2 bottles of {bev}.\nTake one down, pass it around, 1 bottle of {bev} on the wall.\n"
        )
    else:
        print(
            f"{i} bottles of {bev} on the wall, {i} bottles of {bev}.\nTake one down, pass it around, {i - 1} bottles of {bev} on the wall.\n"
        )
