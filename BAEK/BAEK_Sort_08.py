import sys
li = []
for _ in range(int(input())):
    li.append(sys.stdin.readline().strip())
li = list(set(li))
li.sort(key=str)
li.sort(key=lambda x: len(x))
for i in li:
    print(i)