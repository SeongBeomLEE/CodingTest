# Pooling

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

k = n // 2

def pooling(start, end, graph):
    val = []
    for i in range(2):
        for j in range(2):
            val.append(graph[start + i][end + j])
    val = sorted(list(set(val)))[-2]
    return val

def get_result(graph, k):
    new_graph = [[0] * k for i in range(k)]

    for i in range(k):
        for j in range(k):
            new_graph[i][j] = pooling(i * 2, j * 2, graph)

    if k == 1:
        print(new_graph[0][0])
    else:
        get_result(new_graph, int(k/2))

get_result(graph, k)



