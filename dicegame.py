line1 = input()
a1 = int(line1.split()[0])
b1 = int(line1.split()[1])
a2 = int(line1.split()[2])
b2 = int(line1.split()[3])

line2 = input()
a3 = int(line2.split()[0])
b3 = int(line2.split()[1])
a4 = int(line2.split()[2])
b4 = int(line2.split()[3])

ea = a1 + a2
eb = b1 + b2
ga = a3 + a4
gb = b3 + b4

if ga > eb:
  print("Gunnar")
elif ea > gb:
  print("Emma")
else:
  l = ea - ga
  r = gb - eb

  if r == l:
    print("Tie")
  elif (r >= 0 and r > l) or (r < 0 and r < l):
      if max(gb, eb) == eb:
        print("Gunnar")
      else:
        print("Emma")
  else:
    if max(gb, eb) == gb:
      print("Gunnar")
    else:
      print("Emma")

