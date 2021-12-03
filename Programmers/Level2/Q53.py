# 가장 큰 정사각형 찾기
import time
def solution(board):
    ans = 0
    n = len(board)
    m = len(board[0])
    for row in range(1, n):
        for col in range(1, m):
            if board[row][col] == 1:
                board[row][col] = min(board[row - 1][col], board[row - 1][col - 1], board[row][col - 1]) + 1
    for b in board:
        ans = max(ans, max(b))
    return ans ** 2
start = time.time()

board = [[1 for _ in range(1000)] for _ in range(1000)]
board[0][0] = 1
print(solution(board))

end = time.time()
print(end - start)