text = input().lower()

per = "per"
per *= len(text) // 3
ans = len(text)

for i in range(len(text)):
    if text[i] == per[i]:
        ans -= 1

print(ans)