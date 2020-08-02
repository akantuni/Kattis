questions = int(input())
answers = input()
sequences = {
    "Adrian": "ABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCA",
    "Bruno": "BABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABC",
    "Goran": "CCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAA"
}


def check(name):
    counter = -1
    correct = 0
    for letter in answers:
        counter += 1
        if sequences.get(name)[counter] == letter:
            correct += 1
    return correct, name


correctadrian = check("Adrian")
correctbruno = check("Bruno")
correctgoran = check("Goran")

order = [correctadrian, correctbruno, correctgoran]
leader = -1
leadername = ""
for i in order:
    if int(i[0]) > leader:
        leader = int(i[0])
        leadername = i[1]

if int(correctadrian[0]) == int(correctbruno[0]) and int(correctadrian[0]) == int(correctgoran[0]):
    print(str(int(correctadrian[0])) + "\n" + "Adrian" + "\n" + "Bruno" + "\n" + "Goran")
elif int(correctadrian[0]) == int(correctbruno[0]):
    print(str(int(correctadrian[0])) + "\n" + "Adrian" + "\n" + "Bruno")
elif int(correctadrian[0]) == int(correctgoran[0]):
    print(str(int(correctadrian[0])) + "\n" + "Adrian" + "\n" + "Goran")
elif int(correctbruno[0]) == int(correctgoran[0]):
    print(str(int(correctbruno[0])) + "\n" + "Bruno" + "\n" + "Goran")
else:
    print(str(leader) + "\n" + str(leadername))
