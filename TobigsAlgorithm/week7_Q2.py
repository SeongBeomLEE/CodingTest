# 교양 수업은 재미없다구

N = int(input())
M = 1

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

w_visited = [[0] * N for _ in range(N)]
o_visited = [[0] * N for _ in range(N)]

white_cnt = 0
orange_ct = 0

def orange_pooling(row, col, n):
    if o_visited[row][col] == 1: return False

    val = 0
    for i in range(n):
        for j in range(n):
            val += graph[row + i][col + j]

    if val == n**2:
        for i in range(n):
            for j in range(n):
                o_visited[row + i][col + j] = 1

    return val

def white_pooling(row, col, n):
    if w_visited[row][col] == 1: return 1

    val = 0
    for i in range(n):
        for j in range(n):
            val += graph[row + i][col + j]

    if val == 0:
        for i in range(n):
            for j in range(n):
                w_visited[row + i][col + j] = 1

    return val

def result(n, m, w_ct, o_ct):
    for i in range(m):
        for j in range(m):
            if n**2 == orange_pooling(n * i, n * j, n):
                o_ct += 1
            if 0 == white_pooling(n * i, n * j, n):
                w_ct += 1

    if m == N:
        print(w_ct)
        print(o_ct)
        return False
    result(int(n/2), m*2, w_ct, o_ct)

result(N, M, white_cnt, orange_ct)



