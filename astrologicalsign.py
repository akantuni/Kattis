t = int(input())

for i in range(t):
    day, month = input().split()

    if month == "Mar":
        if int(day) >= 21:
            print("Aries")
        else:
            print("Pisces")
    elif month == "Apr":
        if int(day) >= 21:
            print("Taurus")
        else:
            print("Aries")
    elif month == "May":
        if int(day) >= 21:
            print("Gemini")
        else:
            print("Taurus")
    elif month == "Jun":
        if int(day) >= 22:
            print("Cancer")
        else:
            print("Gemini")
    elif month == "Jul":
        if int(day) >= 23:
            print("Leo")
        else:
            print("Cancer")
    elif month == "Aug":
        if int(day) >= 23:
            print("Virgo")
        else:
            print("Leo")
    elif month == "Sep":
        if int(day) >= 22:
            print("Libra")
        else:
            print("Virgo")
    elif month == "Oct":
        if int(day) >= 23:
            print("Scorpio")
        else:
            print("Libra")
    elif month == "Nov":
        if int(day) >= 23:
            print("Sagittarius")
        else:
            print("Scorpio")
    elif month == "Dec":
        if int(day) >= 22:
            print("Capricorn")
        else:
            print("Sagittarius")
    elif month == "Jan":
        if int(day) >= 21:
            print("Aquarius")
        else:
            print("Capricorn")
    elif month == "Feb":
        if int(day) >= 20:
            print("Pisces")
        else:
            print("Aquarius")
