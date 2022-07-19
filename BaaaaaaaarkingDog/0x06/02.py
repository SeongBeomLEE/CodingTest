# https://www.acmicpc.net/problem/18258
# 큐2
import sys
from collections import deque
input = sys.stdin.readline

array = deque([])

for _ in range(int(input())):
    command = input().rstrip().split(" ")
    if command[0] == 'push':
        array.append(command[1])
    elif command[0] == 'pop':
        if array:
            print(array.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(array))
    elif command[0] == 'empty':
        if array:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if array:
            print(array[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if array:
            print(array[-1])
        else:
            print(-1)