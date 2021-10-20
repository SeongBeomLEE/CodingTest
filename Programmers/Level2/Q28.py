# 프렌즈4블록
def solution(m, n, board):
    # [[동 / 북 / 동북] / [서 / 서북/ 북] /  [동 / 동남 / 남] / [서 / 서남 / 남] ]
    dx = [[0, -1, -1], [0, -1, -1], [0, 1, 1], [0, 1, 1]]
    dy = [[1, 0, 1], [-1, -1, 0], [1, 1, 0], [-1, -1, 0]]
    board = [list(i) for i in board]
    answer = 0
    col = len(board[0])
    row = len(board)
    stack = [[x, y] for y in range(n) for x in range(m)]
    _board = [[ 0 for _ in range(n)] for _ in range(m)]
    while True:
        cnt = 0
        for _b, b in zip(_board, board):
            for i, j in zip(_b, b):
                if i == j:
                    cnt += 1
        if cnt == (m*n): break

        _board = [list(i) for i in board]
        del_block = [[0 for _ in range(n)] for _ in range(m)]

        for x, y in stack:
            block = board[x][y]
            cnt = 0
            for _dx, _dy in zip(dx, dy):
                cnt = 0
                for i in range(3):
                    _x, _y = x + _dx[i], y + _dy[i]
                    if -1 < _x and _x < row and -1 < _y and _y < col:
                        if block == board[_x][_y] and block != '#':
                            cnt += 1
                if 3 <= cnt: del_block[x][y] = 1

        for x, y in stack:
            if del_block[x][y] == 1:
                answer += 1
                board[x][y] = '#'

        for x, y in stack[::-1]:
            if board[x][y] == '#':
                _x = x
                while True:
                    _x -= 1
                    if  _x < 0 or  row <= _x or _y < 0 or col <= _y: break
                    else:
                        if board[_x][y] != '#':
                            board[x][y] = board[_x][y]
                            board[_x][y] = '#'
                            break
    return answer

m = 7
n = 2
board = ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]

print(solution(m, n, board), sep = '\n')