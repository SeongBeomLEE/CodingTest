N = int(input())
case = []
for i in range(N):
    A = input()
    case.append(A)

for i in case:
    G = 0
    total = 0
    for s in i:
        if s == 'O':
            G = G + 1
            total = total + G
        if s == 'X':
            G = 0

    print(total)