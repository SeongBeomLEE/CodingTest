# 벽 부수고 이동하기
# 핵심아이디어
# 입력 받은 그래프 + 벽을 부수고 이동했는지 여부 판단 + 현재 이동한 거리가 벽을 부수기 전, 후로 나누어진 그래프

from collections import deque

# N, M = map(int,input().split())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int,input())))

N, M = 6, 4
# 0이 길이고 1이 벽
graph = [
    [0,1,1,0],
    [1,1,1,0],
    [1,0,0,0],
    [0,0,0,0],
    [0,1,1,1],
    [0,0,0,0]
]

# 이동할 상 하 좌 우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    # 시작위치 값을 추가
    queue.append([0, 0, 1])

    # 1개는 벽을 부수지 않고 이동한 거리[x][y][1],
    # 1개는 벽을 부수고 난 후부터 이동한 거리[x][y][1]
    visit = [[[0] * 2 for j in range(M)] for i in range(N)]

    # 첫번째 시작을 1로 함으로써 이동시 마다 1을 더할 때 그 값이 증가하는 것을 나타낼 수 있음
    visit[0][0][1] = 1
    while queue:
        # 가장 먼저 들어온 값부터 탐색 시작
        # breakCount = 1 벽을 부수지 않음
        # breakCount = 0 벽을 부수고 이동한 상태
        x, y, breakCount = queue.popleft()

        # 마지막 위치에 도달 했다면 그 값을 반환
        if x == N - 1 and y == M - 1:
            return visit[x][y][breakCount]

        # 상하좌우 위치를 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                # 벽을 부수지 않고 이동하다가 벽을 만났을 때
                # visit[nx][ny][0] 에 지금까지 이동했던 거리를 넣어주고
                # breakCount를 0으로 바꿔줌으로써 더 이상 벽을 못부수게 함
                if graph[nx][ny] == 1 and breakCount == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    queue.append([nx, ny, 0])
                # graph[nx][ny] == 0 는 이동할 수 있는 길
                # visit[nx][ny][breakCount] == 0 은 아직 이동하지 않은 공간
                elif graph[nx][ny] == 0 and visit[nx][ny][breakCount] == 0:
                    visit[nx][ny][breakCount] = visit[x][y][breakCount] + 1
                    queue.append([nx, ny, breakCount])

                # 이미 벽을 부셨는데 모든 공간이 1로 막혀있다면 반복문에는 아무일도 일어나지 않음

    # 모든 반복문을 돌렸지만
    # 마지막 위치에 도달하지 못했다면
    # 이게 가능한 이유?
    # 반목문은 그냥 반복만 하기 때문에 조건이 맞는 것이 없다면 그냥 돌고 아무일도 일어나지 않음
    return -1

print(bfs())

