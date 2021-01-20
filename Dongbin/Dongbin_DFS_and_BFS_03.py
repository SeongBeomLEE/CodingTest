# 미로 탈출
# # BFS 알고리즘 활용

from collections import deque
# N, M = map(int, input().split())
N, M = 6, 7

# # N개의 값을 입력 받음
# graph = []
# for _ in range(N):
#     graph.append(list(map(int,input())))

# 0은 벽 1은 길
# 도착 위치 N-1, M-1로 가는 최단 거리를 구한다.
graph = [
    [1,1,1,0,1,1,1],
    [1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1],
]
# 이동할 방향 정의
# x의 경우 상하에만 영향을 줌
# y의 경우 좌우에만 영향을 줌
# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x, y):
    # 먼저 들어온 알고리즘 부터 처리를 한다
    queue = deque()
    queue.append((x, y))
    # queue = [] 이 되면 Fasle가 된다
    # 따라서 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 4가지 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로의 공간을 벗어날 경우 무시:
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 움직인 위치가 벽이기 때문에 무시
            if graph[nx][ny] == 0:
                continue
            # 움직인 위치가 길이기 때문에 이동
            if graph[nx][ny] == 1:
                # 현재 위치에서 다음 위치로 이동했기 때문에
                # 1을 더 해줌으로써 움직인 위치 까지의 이동 거리를 구함
                graph[nx][ny] = graph[x][y] + 1
                # 움직인 위치가 존재하기 때문에 값에 넣음
                queue.append((nx, ny))

    # 어디로 가든 최단거리가 나오기 때문에 상관이 없네
    # 도착 위치는 언제나 N-1,M-1 임
    # return graph
    return graph[N-1][M-1]

# 출발 위치는 언제나 0,0 임
# 서로 만나면 종료 한다는 것을 알 수 있음
# 또한 모든 길을 다 탐문했을 때 1이 사라지면 종료 된다는 것을 알 수 있음
print(bfs(0,0))

# for i in bfs(0,0):
#     print(i)