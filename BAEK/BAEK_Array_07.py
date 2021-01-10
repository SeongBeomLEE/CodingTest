N = int(input())
case = []
for i in range(N):
    A = list(map(int,input().split()))
    case.append(A)

for i in case:
    total = 0
    for G in i[1:]:
        total = total + G
    mean = total / i[0]

    index = 0
    for G in i[1:]:
        if G > mean:
            index = index + 1
    print("{:.3f}%".format(index/i[0]*100))