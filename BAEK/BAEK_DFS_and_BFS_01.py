# DFS와 BFS
# DFS
def dfs(graph, v, visited):
    '''
    :param graph: 전체 노드가 연결된 그래프
    :param v: 시작 노드
    :param visited: 0 = 방문 X / 1 = 방문 O
    '''
    # 방문 처리
    visited[v] = 1
    print(v, end=' ')
    # graph의 인덱스 자체가 노드 임
    for i in range(1, N+1):
            # 방문하지 않았고 연결이 되어 있다면 실행
            if visited[i] == 0 and graph[v][i] == 1:
                dfs(graph, i, visited)


# BFS
from collections import deque

def bfs(graph, start, visited):
    '''
    :param graph: 전체 노드가 연결된 그래프
    :param start: 시작 노드
    :param visited: 1 = 방문 X / 0 = 방문 O
    '''
    q = deque([start])
    # 방문 처리
    visited[start] = 0
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N + 1):
            # 방문하지 않았고 연결이 되어 있다면 실행
            if visited[i] == 1 and graph[v][i] == 1:
                q.append(i)
                visited[i] = 0

# N, M, V = map(int, input().split())
# graph = [[0] * (N + 1) for _ in range(N+1)]
# for _ in range(M):
#     i = list(map(int, input().split()))
#     graph[i[0]][i[1]] = 1
#     graph[i[1]][i[0]] = 1

N, M, V = 4, 5, 1
graph = \
[[0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1],
 [0, 1, 0, 0, 1],
 [0, 1, 0, 0, 1],
 [0, 1, 1, 1, 0]]

'''
input
[[1, 2],
 [1, 3],
 [1, 4],
 [2, 4],
 [3, 4]]
'''
'''
output
[[0, 0, 0, 0, 0], 
 [0, 0, 1, 1, 1], 
 [0, 1, 0, 0, 1], 
 [0, 1, 0, 0, 1], 
 [0, 1, 1, 1, 0]]
'''

visited = [0] * (N+1)
dfs(graph, V, visited)
print()
bfs(graph, V, visited)

'''
정답 코드

# DFS
def dfs(graph, v, visited):
    # 방문 처리
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
            if visited[i] == 0 and graph[v][i] == 1:
                dfs(graph, i, visited)


# BFS
from collections import deque
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = 0
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N + 1):
            if visited[i] == 1 and graph[v][i] == 1:
                q.append(i)
                visited[i] = 0

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N+1)]
for _ in range(M):
    i = list(map(int, input().split()))
    graph[i[0]][i[1]] = 1
    graph[i[1]][i[0]] = 1

visited = [0] * (N+1)
dfs(graph, V, visited)
print()
bfs(graph, V, visited)
'''