'''
1. 서로소 집합을 활용하는 방법
2. DFS / BFS 를 활용하는 방법
'''
from collections import deque
def solution(n, computers):
    answer = 0
    graph = []
    visited = [False] * n
    for start_node in range(n):
        if not visited[start_node]:
            q = deque([start_node])
            visited[start_node] = True
            while q:
                a = q.popleft()
                for b, val in enumerate(computers[a]):
                    if val == 1:
                        if not visited[b]:
                            visited[b] = True
                            q.append(b)
            answer += 1
    return answer