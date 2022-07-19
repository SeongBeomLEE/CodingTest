# https://www.acmicpc.net/problem/1021
# 회전하는 큐
import sys
from collections import deque

input = sys.stdin.readline

N, M = input().rstrip().split(" ")
targets = input().rstrip().split(" ")

array = [i + 1 for i in range(int(N))]
answer = 0

for index in range(int(M)):
    target = int(targets[index])

    left_array = deque(array[:])
    right_array = deque(array[:])

    left_count = 0
    right_count = 0

    while True:
        if left_array[0] == target:
            left_array.popleft()
            answer += left_count
            array = list(left_array)
            break
        if right_array[0] == target:
            right_array.popleft()
            answer += right_count
            array = list(right_array)
            break

        left_array.append(left_array.popleft())
        right_array.appendleft(right_array.pop())

        left_count += 1
        right_count += 1

print(answer)