# 사탕 게임
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))

def check(arr):
    N = len(arr)
    answer = 1
    for i in range(N):
        # 열체크
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j - 1]: cnt += 1
            else: cnt = 1
            if answer < cnt: answer = cnt
        # 행체크
        cnt = 1
        for j in range(1, N):
            if arr[j][i] == arr[j - 1][i]: cnt += 1
            else: cnt = 1
            if answer < cnt: answer = cnt

    return answer

answer = max(1, check(arr))
for row in range(N):
    for col in range(N):
        # 열변환
        if col + 1 < N:
            arr[row][col], arr[row][col + 1] = arr[row][col + 1], arr[row][col]
            answer = max(answer, check(arr))
            arr[row][col], arr[row][col + 1] = arr[row][col + 1], arr[row][col]
        # 행변환
        if row + 1 < N:
            arr[row + 1][col], arr[row][col] = arr[row][col], arr[row + 1][col]
            answer = max(answer, check(arr))
            arr[row + 1][col], arr[row][col] = arr[row][col], arr[row + 1][col]

print(answer)