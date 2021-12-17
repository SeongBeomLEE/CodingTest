import copy
def solution(triangle):
    _triangle = copy.deepcopy(triangle)
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            triangle[i + 1][j] = max(_triangle[i + 1][j] + triangle[i][j], triangle[i + 1][j])
            triangle[i + 1][j + 1] = triangle[i + 1][j + 1] + triangle[i][j]

    answer = max(triangle[-1])
    return answer