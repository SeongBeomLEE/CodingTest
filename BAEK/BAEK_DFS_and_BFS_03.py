# 단지번호붙이기
# N = int(input())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input())))


N = 7
graph =[
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0],
]

'''
visited
방문 여부
0 -> 미방문
1 -> 방문
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0]]
'''
visited = [[0]*N for _ in range(N)]

# 상하좌우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col):
    global count
    # 방문체크
    visited[row][col] = 1
    # 단지가 존재하니깐 count 추가
    if graph[row][col] == 1:
        count += 1
    # 상하좌우 탐색
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        # 그래프를 벗어나면 탐색하지 않음
        if 0 <= nx < N and 0 <= ny < N:
            # 방문을 하지 않았고 단지가 존재하면 또 탐색함
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny)

num_list = []
# 아파트 단지수 카운트 체크
count = 0
# 행 값을 넣음
for r in range(N):
    # 열 값을 넣음
    for c in range(N):
        # 단지가 존재하고 방문하지 않았다면 탐색 시작
        if graph[r][c] == 1 and visited[r][c] == 0:
            dfs(r, c)
            # 카운트한 값을 넣어줌
            num_list.append(count)
            # 카운트 초기화
            count = 0
print(len(num_list))
for i in sorted(num_list):
    print(i)

'''
[[0, 1, 1, 0, 0, 0, 0], 
[0, 1, 1, 0, 0, 0, 0], 
[1, 1, 1, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0]]

[[0, 1, 1, 0, 1, 0, 0], 
[0, 1, 1, 0, 1, 0, 1], 
[1, 1, 1, 0, 1, 0, 1], 
[0, 0, 0, 0, 1, 1, 1], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0]]

[[0, 1, 1, 0, 1, 0, 0], 
[0, 1, 1, 0, 1, 0, 1], 
[1, 1, 1, 0, 1, 0, 1], 
[0, 0, 0, 0, 1, 1, 1], 
[0, 1, 0, 0, 0, 0, 0], 
[0, 1, 1, 1, 1, 0, 0], 
[0, 1, 1, 1, 0, 0, 0]]
'''

'''
정답 코드
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

visited = [[0]*N for _ in range(N)]

# 상하좌우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col):
    global count
    visited[row][col] = 1
    if graph[row][col] == 1:
        count += 1
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny)

num_list = []
count = 0
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and visited[r][c] == 0:
            dfs(r, c)
            num_list.append(count)
            count = 0
print(len(num_list))
for i in sorted(num_list):
    print(i)
'''