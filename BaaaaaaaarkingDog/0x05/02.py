# https://www.acmicpc.net/problem/10773
# 제로
import sys
input = sys.stdin.readline

array = []

for _ in range(int(input())):
    command = int(input())
    if command == 0:
        array.pop()
    else:
        array.append(command)

print(sum(array))