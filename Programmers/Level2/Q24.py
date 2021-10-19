# 게임 맵 최단거리
def solution(maps):
    answer = 0
    inf = 101 * 101
    # 동 서 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    d = [[[m, inf] for m in map] for map in maps]
    row = len(maps)
    col = len(maps[0])
    deque = [[0, 0, 1]]

    while deque:
        x, y, dis = deque.pop(0)
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            _dis = dis + 1
            if _x <= -1 or _x >= row or _y <= -1 or _y >= col: continue
            if _x == (row - 1) and _y == (col - 1): return _dis
            if d[_x][_y][0] == 1 and dis < d[_x][_y][1]:
                d[_x][_y][1] = min(dis, d[_x][_y][1])
                deque.append([_x, _y, _dis])

    answer = d[row - 1][col - 1][1]
    return -1 if answer == inf else answer

maps = [[1]*10]*10
# print(maps[99][99], sep='\n')
print(solution(maps), sep='\n')