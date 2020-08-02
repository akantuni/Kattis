n = int(input())

for i in range(n):
    array = list(map(int, input().split()))
    sum = 0
    counter = 0
    for number in array:
        num2 = array[counter + 1]
        if number == 0 or num2 == 0:
            break
        elif num2 > number * 2:
            sum += num2 - number * 2
        counter += 1
    print(sum)