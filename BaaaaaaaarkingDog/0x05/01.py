# https://www.acmicpc.net/problem/10828
# 스택
import sys
input = sys.stdin.readline

array = []

for _ in range(int(input())):
    command = input().rstrip().split(" ")
    if command[0] == 'push':
        array.append(command[1])
    elif command[0] == 'pop':
        if array:
            print(array.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(array))
    elif command[0] == 'empty':
        if array:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if array:
            print(array[-1])
        else:
            print(-1)