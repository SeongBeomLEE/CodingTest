# 회장님의 프러포즈
# https://hooongs.tistory.com/330

array = [65, 64, 67, 60, 0, 0]
n = 6

from collections import deque

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

stack = deque()
answer = 0

for i in range(n):
    while len(stack) != 0 and array[stack[-1]] > array[i]:
        tmp = stack.pop()

        if len(stack) == 0:
            width = i
        else:
            width = i - stack[-1] - 1
        answer = max(answer, width * array[tmp])

    stack.append(i)

while len(stack) != 0:
    tmp = stack.pop()

    if len(stack) == 0:
        width = n

    else:
        width = n - stack[-1] - 1

    answer = max(answer, width * array[tmp])

print(answer)