# 플로이드 워셜 알고리즘
# 모든 노드에서 다른 모드 노드 까지의 최단 경로를 모두 계산
import sys

# 무힌을 의미하는 값으로 10억을 설정
INF = 987654321

# 노드의 개수, 간선의 개수를 입력받기
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
# 2차원 리스트(그래프 표현)을 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
# a -> 출발 노드, b -> 도착 노드
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값을 초가화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우
        if graph[a][b] == INF:
            print(0, end=" ")
        else: print(graph[a][b], end= " ")
    print()
