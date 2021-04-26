# IP채굴기
# 핵심 아이디어
# 상하좌우 모든 방향을 움직이는 함수를 만든다.
# count가 8이 되면 현재까지의 결과를 넣는다.
# 위치를 벗어나면 그만둔다.
# 모든 좌표에 대한 경우의 수를 구한다.

arr = []
for _ in range(4):
    val = input().split()
    arr.append(val)

# 상하좌우 지정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


result_li = []
def bfs(x, y, result, count):
    if x <= -1 or x >= 4 or y <= -1 or y >= 4:
        return False
    # 현재의 결과룰을 더 해주는 위치가 매우 중요함
    result += str(arr[x][y])
    if count == 8 :
        result_li.append(result)
        return False
    # 상하좌우 중 하나의 방향으로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        bfs(nx, ny, result, count+1)

for x in range(4):
    for y in range(4):
        bfs(x, y, "", 1)

# set문을 통해서 중복은 제거해줌
print(len(set(result_li)))

