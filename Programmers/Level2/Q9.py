# 행렬 테두리 회전하기

# 방법1
from collections import deque
def solution(rows, columns, queries):
    m = [[col + row * columns for col in range(1, columns + 1)] for row in range(rows)]
    answer = []
    for q in queries:
        x1, y1, x2, y2 = q
        x, y = x1, y1
        idx = 0
        stack = deque()
        rot = ((x2-(x1 - 1)) * (y2-(y1 - 1))) - (((x2 - 1)-((x1 + 1) - 1)) * ((y2 - 1)-((y1 + 1) - 1)))
        if rot == 0 :
            answer.append(m[x - 1][y - 1])
        else:
            for _ in range(rot):
                stack.append(m[x - 1][y - 1])
                if x == x1 and y != y2:
                    y += 1
                elif y == y2 and x != x2:
                    x += 1
                elif x == x2 and y != y1:
                    y -= 1
                elif y == y1 and x != x1:
                    x -= 1
            answer.append(min(stack))
            y = y + 1
            while stack:
                m[x - 1][y - 1] = stack.popleft()
                if x == x1 and y != y2:
                    y += 1
                elif y == y2 and x != x2:
                    x += 1
                elif x == x2 and y != y1:
                    y -= 1
                elif y == y1 and x != x1:
                    x -= 1
    return answer

# 방법2
def solution(rows, columns, queries):
    m = [[col + row * columns for col in range(1, columns + 1)] for row in range(rows)]
    answer = []
    for q in queries:
        x1, y1, x2, y2 = q
        x, y = x1, y1
        idx = 0
        stack = []
        rot = ((x2-(x1 - 1)) * (y2-(y1 - 1))) - (((x2 - 1)-((x1 + 1) - 1)) * ((y2 - 1)-((y1 + 1) - 1)))
        if rot == 0 :
            answer.append(m[x - 1][y - 1])
        else:
            for _ in range(rot):
                stack.append(m[x - 1][y - 1])
                if len(stack) >= 2:
                    m[x - 1][y - 1] = stack[idx]
                    idx += 1
                if x == x1 and y != y2:
                    y += 1
                elif y == y2 and x != x2:
                    x += 1
                elif x == x2 and y != y1:
                    y -= 1
                elif y == y1 and x != x1:
                    x -= 1
            m[x - 1][y - 1] = stack[idx]
            answer.append(min(stack))
    return answer

rows = 100
columns = 97
queries = [[1,1,100,97]]
print(solution(rows, columns, queries))
