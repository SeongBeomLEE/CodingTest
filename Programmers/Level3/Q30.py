# 경주로 건설
'''
https://programmers.co.kr/learn/courses/30/lessons/67259

최소값일 수 있는 경우가 여러개 존재할 수 있기 때문에
각 위치에 도달하는 cost를 모두 저장하는 것이 필요함

'''

from collections import deque

def solution(board):
    INF = 987654321
    N = len(board)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cost_borad = [[INF] * N for _ in range(N)]
    q = deque([[0, 0, -1, 0]])
    answer = []
    while q:
        x, y, direction, cost = q.popleft()
        if x == N - 1 and y == N - 1:
            answer.append(cost)

        for d, i in enumerate(range(4)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1:
                add_cost = 100 if (d == direction or direction == -1) else 600
                if cost_borad[nx][ny] < cost + add_cost - 400:
                    continue
                cost_borad[nx][ny] = cost + add_cost
                q.append([nx, ny, d, cost + add_cost])

    return min(answer)

board = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
print(solution(board))