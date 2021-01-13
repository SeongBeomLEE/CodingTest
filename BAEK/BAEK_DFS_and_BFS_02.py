# 바이러스
# DFS
def dfs(graph, v, visited):
    '''
    :param graph: 전체 노드가 연결된 그래프
    :param v: 시작 노드
    :param visited: 0 = 방문 X / 1 = 방문 O
    '''
    # 방문 처리
    visited[v] = 1
    # graph의 인덱스 자체가 노드 임
    for i in range(1, N+1):
            # 방문하지 않았고 연결이 되어 있다면 실행
            if visited[i] == 0 and graph[v][i] == 1:
                dfs(graph, i, visited)

# N = int(input())
# graph = [[0] * (N + 1) for _ in range(N+1)]
# for _ in range(int(input())):
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

visited = [0] * (N+1)
dfs(graph, 1, visited)
print(sum(visited) - 1)

'''
정답 코드

def dfs(graph, v, visited):
    visited[v] = 1
    for i in range(1, N+1):
            if visited[i] == 0 and graph[v][i] == 1:
                dfs(graph, i, visited)

N = int(input())
graph = [[0] * (N + 1) for _ in range(N+1)]
for _ in range(int(input())):
    i = list(map(int, input().split()))
    graph[i[0]][i[1]] = 1
    graph[i[1]][i[0]] = 1

visited = [0] * (N+1)
dfs(graph, 1, visited)
print(sum(visited) - 1)
'''