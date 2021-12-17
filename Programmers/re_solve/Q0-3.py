# 네트워크
# DFS/BFS 활용
def solution(n, computers):
    answer = 0
    visit = [False] * n

    for a in range(n):
        if not visit[a]:
            q = [a]
            while q:
                a = q.pop(0)
                if visit[a]: continue
                visit[a] = True
                for b in range(n):
                    if a != b and computers[a][b] == 1:
                        if not visit[b]: q.append(b)
            answer += 1

    return answer
n = 5
computers = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]]
print(solution(n, computers))