n = int(input())

for i in range(n):
    details = input().split()
    name = details[0]
    # ps = year the student began post-secondary studies
    ps = int(details[1].split("/")[0])
    # yob = "year of birth"
    yob = int(details[2].split("/")[0])
    courses = int(details[3])

    if ps >= 2010:
        print(name, "eligible")
    elif yob >= 1991:
        print(name, "eligible")
    elif courses >= 41:
        print(name, "ineligible")
    else:
        print(name, "coach petitions")
