testcases = input().split()
n = int(testcases[0])
q = int(testcases[1])
companies = input().split()
memo = {}

for index, val in enumerate(companies):
    memo[index + 1] = val

for i in range(q):
    case = input().split()
    query = int(case[0])
    a = int(case[1])
    b = int(case[2])

    if query == 1:
        memo[a] = b

    elif query == 2:
        print(abs(int(memo[a]) - int(memo[b])))
