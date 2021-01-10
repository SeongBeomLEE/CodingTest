# 내가 푼 방법
def right(y):
    if y == N-1 : return y # 더 이상 갈 곳이 없을때는 원래 값을 출력
    return y + 1

def left(y):
    if y == 0: return y # 더 이상 갈 곳이 없을때는 원래 값을 출력
    return y - 1

def up(x):
    if x == 0 : return x # 더 이상 갈 곳이 없을때는 원래 값을 출력
    return x - 1

def down(x):
    if x == N-1: return x # 더 이상 갈 곳이 없을때는 원래 값을 출력
    return x + 1

# N = int(input())
N = 5
# road = input().split()
road= ["D", "D", "D", "D", "D", "D", "D"]
li = [[(j, i) for i in range(1, N+1)] for j in range(1, N+1)]

x, y = 0, 0
for r in road:
    if r == "R": y = right(y)
    if r == "L": y = left(y)
    if r == "U": x = up(x)
    if r == "D": x = down(x)

r_x, r_y = li[x][y]
print(r_x, r_y)

# 책에 있는 방법