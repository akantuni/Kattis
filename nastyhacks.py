n = int(input())


ans = 0
while n > 0:
  line2 = input()
  r = int(line2.split()[0])
  e = int(line2.split()[1])
  c = int(line2.split()[2])

  ans = e - c
  if ans > r:
    print("advertise")
  if ans < r:
    print("do not advertise")
  if ans == r:
    print("does not matter")
  n = n - 1
