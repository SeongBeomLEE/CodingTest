# 게임 개발
# N, M = map(int, input().split())
N, M = 4, 4

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*M for _ in range(N)]
'''
[[0, 0, 0, 0], 
[0, 0, 0, 0], 
[0, 0, 0, 0], 
[0, 0, 0, 0]]
'''
# 현재 캐릭터의 X죄표, Y좌표 방향을 입력받기
# x, y, direction = map(int, input().split())
x, y, direction = 1, 1, 0

# 현재 좌표 방문 처리
d[x][y] = 1
'''
[[0, 0, 0, 0], 
[0, 1, 0, 0], 
[0, 0, 0, 0], 
[0, 0, 0, 0]]
'''

# 전체 맵 정보 입력받기
array = []
# for _ in range(N):
#     array.append(list(map(int, input().split())))

array = [[1,1,1,1],
         [1,0,0,1],
         [1,1,0,1],
         [1,1,1,1]]

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
# 시물레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 방문 처리
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else: turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else: break
        turn_time = 0
print(count)

'''
방문여부
[[0, 0, 0, 0], 
[0, 1, 1, 0], 
[0, 0, 1, 0], 
[0, 0, 0, 0]]
'''

'''
갈 수 있는 곳 : 0
[[1, 1, 1, 1], 
[1, 0, 0, 1], 
[1, 1, 0, 1], 
[1, 1, 1, 1]]
'''
