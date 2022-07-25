# https://www.acmicpc.net/problem/15683
# 감시
'''

0 <- 빈칸
1 ~ 5 <- CCTV
6 <- 벽
# <- 감시할 수 있는 영역

- 감시 영역은 벽을 통과할 수 없음
- 감시 영역은 CCTV를 통과할 수 있음
- 각 CCTV 번호에 따른 서로 다른 탐색
- 방향에 따른 변환 생성
- 사각 지대의 최소 크기를 출력 (결국 최소 0의 개수를 출력하는 것)
- 1, 3, 4번은 4번 회전 가능
- 2번은 2번 회전 가능
- 5번 회전 필요 없음
- 직진하면서 0 번에 # 을 채우는 함수 생성 (시작 위치, 방향이 parameter)

'''
import sys
import copy

# 방향에 따른 # 채우기
def fill_maps(row, col, direction, maps):
    global N, M
    while True:
        if row < 0 or row == N or col < 0 or col == M: break
        if maps[row][col] == '6': break # 벽에 부딪힘
        if maps[row][col] == '0': maps[row][col] = '#'

        # 위치 이동
        if direction == 'up': row -= 1
        elif direction == 'right': col += 1
        elif direction == 'down': row += 1
        elif direction == 'left': col -= 1
    
    return maps

def solution(idx, maps):
    global answer, CCTV_count, CCTV_stations
    if idx == CCTV_count:
        zero_count = 0
        for row in range(N):
            for col in range(M):
                if maps[row][col] == '0':
                    zero_count += 1
        answer.append(zero_count)
        return

    row, col, CCTV_type = CCTV_stations[idx]
    new_maps = copy.deepcopy(maps)

    if CCTV_type == '1':
        for direction in ['up', 'right', 'down', 'left']:
            maps = copy.deepcopy(new_maps)
            maps = fill_maps(row, col, direction, maps)
            solution(idx + 1, maps)

    if CCTV_type == '2':
        for direction in [('left', 'right'), ('up', 'down')]:
            maps = copy.deepcopy(new_maps)
            maps = fill_maps(row, col, direction[0], maps)
            maps = fill_maps(row, col, direction[1], maps)
            solution(idx + 1, maps)
    
    if CCTV_type == '3':
        for direction in [('up', 'right'), ('right', 'down'), ('down', 'left'), ('left', 'up')]:
            maps = copy.deepcopy(new_maps)
            maps = fill_maps(row, col, direction[0], maps)
            maps = fill_maps(row, col, direction[1], maps)
            solution(idx + 1, maps)
    
    if CCTV_type == '4':
        for direction in [('left', 'up', 'right'), ('up', 'right', 'down'), ('right', 'down', 'left'), ('down', 'left', 'up')]:
            maps = copy.deepcopy(new_maps)
            maps = fill_maps(row, col, direction[0], maps)
            maps = fill_maps(row, col, direction[1], maps)
            maps = fill_maps(row, col, direction[2], maps)
            solution(idx + 1, maps)
    
    if CCTV_type == '5':
        for direction in [('up', 'right', 'down', 'left')]:
            maps = copy.deepcopy(new_maps)
            maps = fill_maps(row, col, direction[0], maps)
            maps = fill_maps(row, col, direction[1], maps)
            maps = fill_maps(row, col, direction[2], maps)
            maps = fill_maps(row, col, direction[3], maps)
            solution(idx + 1, maps)

input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

maps = []
for i in range(N):
    maps.append(input().rstrip().split(" "))

# CCTV 위치 파악
CCTV_stations = []
for row in range(N):
    for col in range(M):
        if maps[row][col] != '0' and maps[row][col] != '6':
            CCTV_stations.append((row, col, maps[row][col]))

CCTV_count = len(CCTV_stations)
answer = []

solution(0, maps)
print(min(answer))