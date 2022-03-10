# 소문난 칠공주
def get_answer(ans, depth = 0, S = 0, Y = 0):
    if Y > 3: return False
    if depth == 6:
        answer.add(tuple(sorted(ans)))
    if depth < 6:
        # 현재 까지 탐색한 모든 노드에서 출발하는 것이 이 문제의 핵심
        for node in ans:
            x, y = node
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in ans:
                    if maps[nx][ny] == 'S':
                        get_answer(ans[:] + [(nx, ny)], depth = depth + 1, S = S + 1, Y = Y)
                    else:
                        get_answer(ans[:] + [(nx, ny)], depth = depth + 1, S = S, Y = Y + 1)

maps = []
for _ in range(5):
    maps.append(list(input()))

answer = set()
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

for row in range(5):
    for col in range(5):
        if maps[row][col] == 'S':
            get_answer([(row, col)], depth = 0, S = 1, Y = 0)

print(len(answer))