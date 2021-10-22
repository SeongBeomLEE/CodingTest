# 빛의 경로 사이클
def solution(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[[0 for j in range(4)] for _ in range(cols + 1)] for i in range(rows + 1)]

    answer = []
    for i in range(rows):
        for j in range(cols):
            # 위 - 0 아래 - 1 왼 - 2 오 - 3
            for start in range(4):
                x, y = i, j
                move = start
                step = 0
                while True:
                    # 방문 처리
                    visited[x][y][move] = 1
                    step += 1

                    if move == 0:
                        x -= 1
                    elif move == 1:
                        x += 1
                    elif move == 2:
                        y -= 1
                    elif move == 3:
                        y += 1

                    if x < 0:
                        x = rows - 1
                    elif x >= rows:
                        x = 0
                    if y < 0:
                        y = cols - 1
                    elif y >= cols:
                        y = 0

                    if move == 0:
                        if grid[x][y] == 'L': move = 3
                        elif grid[x][y] == 'R': move = 2

                    elif move == 1:
                        if grid[x][y] == 'L': move = 2
                        elif grid[x][y] == 'R': move = 3

                    elif move == 2:
                        if grid[x][y] == 'L': move = 0
                        elif grid[x][y] == 'R': move = 1

                    elif move == 3:
                        if grid[x][y] == 'L': move = 1
                        elif grid[x][y] == 'R': move = 0

                    if visited[x][y][move] != 0:
                        if rows * cols == 1:
                            answer.append(step)
                        else:
                            if step != 1:
                                answer.append(step)
                        break
    return sorted(answer)

grid = ["RR"]
print(solution(grid))
