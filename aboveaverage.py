n = int(input())
average = 0
aa = []

for i in range(n):
    s = input()
    students = int(s.split()[0])
    grades = s.split()[1:]
    for grade in grades:
        average += int(grade)
    for grade in grades:
        if int(grade) > average / students:
            aa.append(grade)
        else:
            continue
    average = 0
    print(str("{:.3f}".format((len(aa) / students) * 100)) + "%")
    aa = []
