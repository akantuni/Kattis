cards = input().split()
gold = int(cards[0])
silver = int(cards[1])
copper = int(cards[2])
victory = {"Province": 8, "Duchy": 5, "Estate": 2}
costtreasure = {"Gold": 6, "Silver": 3, "Copper": 0}
bptreasure = {"Gold": 3, "Silver": 2, "Copper": 1}

total = gold * bptreasure["Gold"] + silver * bptreasure["Silver"] + copper * bptreasure["Copper"]

if total < 2:
    print("Copper")
elif total >= 8:
    print("Province or Gold")
elif 5 <= total < 8:
    if total >= 6:
        print("Duchy or Gold")
    else:
        print("Duchy or Silver")
elif total < 5:
    if total >= 3:
        print("Estate or Silver")
    else:
        print("Estate or Copper")


