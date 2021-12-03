# 방문 길이
def solution(dirs):
    x, y = 0, 0
    ans = []
    for dir in dirs:
        _x, _y = x, y
        if dir == 'U' and y < 5: y += 1
        elif dir == 'D' and y > -5: y -= 1
        elif dir == 'R' and x < 5: x += 1
        elif dir == 'L' and x > -5: x -= 1
        if f'({_x}, {_y})' != f'({x}, {y})':
            if f'({x}, {y}) -> ({_x}, {_y})' not in ans:
                ans.append(f'({_x}, {_y}) -> ({x}, {y})')
    answer = len(set(ans))
    return answer
dirs = "LURDLURDLURDR"
print(solution(dirs))