x = int(input())

animal_sounds = []

for i in range(x):
    sounds = input().split()

    while True:
        line = input()
        if line == "what does the fox say?":
            break
        sound = line.split()[2]
        animal_sounds.append(sound)

        fox_noise = []
        for sound in sounds:
            if sound not in animal_sounds:
                fox_noise.append(sound)

    print(" ".join(fox_noise))
