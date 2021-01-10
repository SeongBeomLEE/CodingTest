import sys
li = []
for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    li.append([y, x])
li.sort()
for i in range(len(li)):
    print(li[i][1], li[i][0])