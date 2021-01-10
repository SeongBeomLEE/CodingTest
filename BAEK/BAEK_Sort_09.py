import sys
li = []
for idx in range(int(input())):
    x, y = sys.stdin.readline().split()
    li.append((int(x), str(y), int(idx)))
li.sort(key= lambda x: (x[0], x[2]))
for i in li:
    print(i[0], i[1])