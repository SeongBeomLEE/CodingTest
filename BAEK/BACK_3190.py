# 뱀
from collections import deque

N = int(input())
arr = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

L = int(input())
direction_change_information = deque([])
for _ in range(L):
    time, direction = input().split()
    direction_change_information.append([int(time), direction])

head = 0
answer = 0
snake_index = deque([[0, 0]])
while True:
    r, c = snake_index.pop()

    # 뱀의 방향 변환 여부
    if direction_change_information:
        if answer == direction_change_information[0][0]:
            time, direction = direction_change_information.popleft()

            # 좌우
            if direction == 'D':
                head += 1
            elif direction == 'L':
                head -= 1

            if 3 < head: head = 0
            if head < 0: head = 3

    # 이동
    dr, dc = r, c
    if head == 0: dc += 1
    elif head == 1: dr += 1
    elif head == 2: dc -= 1
    elif head == 3: dr -= 1

    # 시간
    answer += 1

    # 이동 규칙
    snake_index.append([r, c])
    if dr < 0 or N <= dr or dc < 0 or N <= dc or [dr, dc] in snake_index: break
    if arr[dr][dc] == 1:
        arr[dr][dc] = 0
        snake_index.append([dr, dc])
    else:
        snake_index.popleft()
        snake_index.append([dr, dc])

print(answer)
