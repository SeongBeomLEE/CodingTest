# 거리두기 확인하기
def solution(places):
    answer = []
    for place in places:
        m = [[ 0 for _ in range(5)] for _ in range(5)]
        for rows, pp in enumerate(place):
            for cols, p in enumerate(pp):
                if p == 'P':
                    m[rows][cols] -= 1
                    if cols == 0 or cols == 4:
                        if cols == 0:
                            m[rows][cols + 1] -= 1  # 우
                        if cols == 4:
                            m[rows][cols - 1] -= 1  # 죄
                        if rows == 0:
                            m[rows + 1][cols] -= 1 # 하
                        if 0 < rows < 4:
                            m[rows - 1][cols] -= 1  # 상
                            m[rows + 1][cols] -= 1  # 하
                        if rows == 4:
                            m[rows - 1][cols] -= 1  # 상
                    elif rows == 0 or rows == 4:
                        if rows == 0:
                            m[rows + 1][cols] -= 1  # 하
                        if rows == 4:
                            m[rows - 1][cols] -= 1  # 상
                        if cols == 0:
                            m[rows][cols + 1] -= 1  # 우
                        if 0 < cols < 4:
                            m[rows][cols + 1] -= 1  # 우
                            m[rows][cols - 1] -= 1  # 좌
                        if cols == 4:
                            m[rows][cols - 1] -= 1  # 좌
                    else:
                        m[rows - 1][cols] -= 1  # 상
                        m[rows + 1][cols] -= 1  # 하
                        m[rows][cols + 1] -= 1  # 우
                        m[rows][cols - 1] -= 1  # 좌
                if p == 'X':
                    m[rows][cols] += 10
        temp = False
        for rows in m:
            for cols in rows:
                if cols <= -2:
                    temp = True
                    break
            if temp: break

        if temp: answer.append(0)
        else: answer.append(1)
    return answer

places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]

print(solution(places))