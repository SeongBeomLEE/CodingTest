# 행렬의 곱셈
def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    iters = len(arr1[0])
    answer = [[0] * m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            ans = 0
            for i in range(iters):
                ans += arr1[row][i] * arr2[i][col]
            answer[row][col] = ans
    return answer
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = 	[[3, 3], [3, 3]]
print(solution(arr1, arr2))