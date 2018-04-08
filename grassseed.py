n = float(input())
x = float(input())

ans = 0
while x > 0:
  line1 = input()
  z = float(line1.split()[0])
  y = float(line1.split()[1])
  
  ans = ans + (z * y * n)
  
  x = x - 1

print(ans)
  
  
