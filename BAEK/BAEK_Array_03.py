A = int(input())
B = int(input())
C = int(input())

ABC = str(A*B*C)
count = [0,0,0,0,0,
         0,0,0,0,0]

for i in ABC:
    if i == "0":
        count[0] = count[0] + 1
    if i == "1":
        count[1] = count[1] + 1
    if i == "2":
        count[2] = count[2] + 1
    if i == "3":
        count[3] = count[3] + 1
    if i == "4":
        count[4] = count[4] + 1
    if i == "5":
        count[5] = count[5] + 1
    if i == "6":
        count[6] = count[6] + 1
    if i == "7":
        count[7] = count[7] + 1
    if i == "8":
        count[8] = count[8] + 1
    if i == "9":
        count[9] = count[9] + 1

for i in count:
    print(i)