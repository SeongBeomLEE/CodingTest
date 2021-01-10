import sys
li = []
for _ in range(int(input())):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort()
for i in range(len(li)):
    print(li[i][0], li[i][1])