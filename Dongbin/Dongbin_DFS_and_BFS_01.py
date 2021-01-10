# 음료수 얼려 먹기
# DFS 깊이 우선 탐색 알고리즘을 활용

# N, M = map(int, input().split())
N, M = 4, 5


# N x M 의 2차원 리스트를 받음
# # N개의 값을 입력 받음
# graph = []
# for _ in range(N):
#     graph.append(list(map(int,input())))

graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

def dfs(x, y):
    # x는 행, y는 열
    # 따라서
    # x가 0보다 작거나 N 보다 크거나 같다면 범위를 벗어남
    # y가 0보다 작거나 M 보다 크거나 같다면 범위를 벗어남
    if x <= -1 or x >= N or y <= -1 or y >= M: return False
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리 헤야함 (0을 1로 바꿔주면 가능)
        graph[x][y] = 1
        # 위 방문처리
        dfs(x-1, y)
        # 아래 방문처리
        dfs(x+1, y)
        # 좌측 방문처리
        dfs(x, y-1)
        # 우측 방문처리
        dfs(x, y +1)
        # 모두 방문을 했다면 True를 반환
        return True
    # 값이 0이 아니라는 것은 이미 방문한 노드이거나 원래부터 1이 었던 노드
    return False

count = 0
# 행을 반복
for i in range(N):
    # 열을 반복
    for j in range(M):
        # 값이 0이었던 노드 중에 인접 노드를 모두 방문하면 True를 반환
        if dfs(i, j) == True:
            count += 1

print(count)