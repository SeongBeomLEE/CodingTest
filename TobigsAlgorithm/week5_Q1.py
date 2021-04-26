# 경태는 알고리즘 마스터~

node_count = int(input())
graph = []

for _ in range(node_count):
    graph.append(list(map(int, input().split())))

result_li = []
def getNodeCount(node, idx, result):
    result += graph[node][idx]
    if node == node_count - 1 :
        result_li.append(result)
        return False
    return getNodeCount(node + 1, idx, result), getNodeCount(node + 1, idx + 1, result)

getNodeCount(0, 0, 0)
# 그래프를 타고 내려오면서 최대값을 반환
print(max(result_li))



