# N-Queen
'''
본 문제의 핵심은 행체크, 열체크, 대각선 체크 / pypy3로 제출해야 시간초과가 나지 않음

- 행체크
재귀를 이용하여 같은 행에는 퀸을 놓지 못하도록 함

- 열체크
board는 [행] = 열
즉 board = [1, 2, 3, 4] 가 있다면 borad[0] 은 0행 1열에 퀸이 존재한다는 것을 의미
board[k] == board[depth] 를 이용해 열체크
board[0] == board[1] 이 같은 값을 가진다면 같은 열에 퀸이 존재한다는 것을 의미
따라서 k는 깊이 만큼만 반복

- 대각선 체크
abs(k - depth) == abs(board[k] - board[depth]) 를 이용해 대각선 체크
행 - 행 에 절대 값과 열 - 열의 절대 값이 같다면 두 퀸은 대각선상에 위치함
'''
answer = 0
N = int(input())

def get_answer(depth, board):
    global answer
    if depth == N:
        answer += 1
        return False
    else:
        for col in range(N):
            board[depth] = col

            ko = True
            for k in range(depth):
                if board[k] == board[depth] or (abs(k - depth) == abs(board[k] - board[depth])):
                    ko = False
                    break
            if ko:
                get_answer(depth = depth + 1, board = board)

get_answer(depth = 0, board = [0] * N)

print(answer)


