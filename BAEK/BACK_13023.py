# ABCDE
# 길이가 5인 그래프가 존재한다면 ABCDE의 관계가 성립함

N, M = map(int, input().split())
linked = [[] for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    linked[i] += [j]
    linked[j] += [i]

def dfs(i, depth):
    visit[i] = True
    if depth == 5:
        return True
    for j in linked[i]:
        if not visit[j]:
            if dfs(j, depth + 1):
                return True
            visit[j] = False

visit = [False] * N
answer = False
for i in range(N):
    if dfs(i, 1):
        answer = True
    visit[i] = False
    if answer: break

print(1 if answer else 0)





