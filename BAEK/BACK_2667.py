# 단지번호붙이기
from collections import deque

answer = []
array = []

N = int(input())
for _ in range(N):
    array.append(list(map(int, list(input()))))

# 동, 서, 남, 북
d_col = [1, -1, 0, 0]
d_row = [0, 0, 1, -1]

visited_array = [[True if v == 1 else False for v in val] for val in array]

for r in range(N):
    for c in range(N):
        if visited_array[r][c]:
            q = deque([[r, c]])
            visited_array[r][c] = False
            num = 1
            while q:
                row, col = q.popleft()
                for i in range(4):
                    _row = row + d_row[i]
                    _col = col + d_col[i]
                    if 0 <= _row < N and 0 <= _col < N:
                        if visited_array[_row][_col]:
                            visited_array[_row][_col] = False
                            num += 1
                            q.append([_row, _col])
            answer.append(num)

answer.sort()
print(len(answer))
for i in answer:
    print(i)