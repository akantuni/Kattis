x = int(input())

ans = 0
while x > 0:
  y = int(input())
  z = y % 10
  ans = (y // 10) ** z + ans
  x -= 1
  
print(ans)
