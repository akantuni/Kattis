import datetime

n = input()
d = int(n.split()[0])
m = int(n.split()[1])

days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
day = datetime.date(2009, m, d)

print(days.get(day.weekday()))
