line1 = input()
line2 = input()
line3 = input()
line4 = input()
line5 = input()

w = line1.split()[0]
x = line1.split()[1]
y = line1.split()[2]
z = line1.split()[3]


a = line2.split()[0]
b = line2.split()[1]
c = line2.split()[2]
d = line2.split()[3]


e = line3.split()[0]
f = line3.split()[1]
g = line3.split()[2]
h = line3.split()[3]


i = line4.split()[0]
j = line4.split()[1]
k = line4.split()[2]
l = line4.split()[3]

q = line5.split()[0]
r = line5.split()[1]
s = line5.split()[2]
t = line5.split()[3]

m = (int(w) + int(x) + int(y) + int(z))
n = (int(a) + int(b) + int(c) + int(d))
o = (int(e) + int(f) + int(g) + int(h))
p = (int(i) + int(j) + int(k) + int(l))
v = (int(q) + int(r) + int(s) + int(t))

if (m > n) and (m > o) and (m > p) and (m > v):
  print("1", m) 
  
elif (n > m) and (n > o) and (n > p) and (n > v):
  print("2", n)
  
elif (o > m) and (o > n) and (o > p) and (o > v):
  print("3", o)
  
elif (p > m) and (p > n) and (p > o) and (p > v):
  print("4", p)
  
elif (v > m) and (v > n) and (v > o) and (v > p):
  print("5", v) 
