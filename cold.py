n = int(input())
line = input()
arr = line.split()

ans = 0
for i in range(n):
  x = int(arr[i])
  if x < 0:
    ans = ans + 1

print(ans)
