line = input()
n = int(line.split()[0])
w = int(line.split()[1])
h = int(line.split()[2])

while n > 0:
  l = int(input())
  
  if l * l <= w * w + h * h:
    print("DA")
  else:
    print("NE")
    
  n = n - 1
