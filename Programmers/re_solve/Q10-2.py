'''
일단은

2번이 1번을 이기면 / 2번은 1번을 이긴 모든 선수들의 경기를 이길 수 있음

A 선수가 B 선수를 이기면 / B 선수가 이긴 모든 선수를 이긴다

플로이드 워셜 알고리즘의 시간복잡도는 n^3 이고,
이에 최대 시복은 1000000 이기 때문에 플로이드워셜 알고리즘 활용 가능
'''
def solution(n, results):
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for a, b in results:
        graph[a - 1][b - 1] += 1
        graph[b - 1][a - 1] -= 1

    # 플로이드 워셜 알고리즘 활용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 두 개의 그래프가 서로 연결되어 있다면
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1

    answer = 0
    for i in graph:
        if i.count(0) == 1:
            answer += 1

    return answer