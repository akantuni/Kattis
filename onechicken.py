line = input()

n = int(line.split(" ")[0])
m = int(line.split(" ")[1])

ans = m - n

if ans > 0:
    if ans == 1:
        print("Dr. Chaz will have", ans, "piece of chicken left over!")
    else:
        print("Dr. Chaz will have", ans, "pieces of chicken left over!")
elif abs(ans) == 1:
    print("Dr. Chaz needs", (ans * -1), "more piece of chicken!")
else:
    print("Dr. Chaz needs", (ans * -1), "more pieces of chicken!")
