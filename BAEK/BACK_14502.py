# 연구소
# N, M의 차원이 작기 때문에
# 완전 탐색으로 벽을 세울 수 있는 모든 경우의 수를 구함

from itertools import combinations
import copy
from collections import deque

answer = 0
N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

wall_index_list = []
virus_index_list = []
for r in range(len(maps)):
    for c in range(len(maps[0])):
        if maps[r][c] == 0:
            wall_index_list.append([r, c])
        if maps[r][c] == 2:
            virus_index_list.append([r, c])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

wall_index_list = list(combinations(wall_index_list, 3))
for wall_index in wall_index_list:
    _maps = copy.deepcopy(maps)

    for r, c in wall_index:
        _maps[r][c] = 1

    for idx in virus_index_list:
        q = deque([idx])
        while q:
            r, c = q.popleft()
            for i in range(4):
                nx = r + dx[i]
                ny = c + dy[i]
                if 0 <= nx < N and 0 <= ny < M and _maps[nx][ny] != 1 and _maps[nx][ny] == 0:
                    _maps[nx][ny] = 2
                    q.append([nx, ny])

    cnt_0 = 0
    for m in _maps:
        cnt_0 += m.count(0)
    answer = max(answer, cnt_0)

print(answer)