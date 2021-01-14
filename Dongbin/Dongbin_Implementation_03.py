# 왕실의 나이트
# data = input()
data = 'a1'
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

# 나이트가 움직일 수 있는 8가지 방향 (행, 열)
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

count = 0

for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]
    if (1 <= nrow <= 8) and (1 <= ncol <= 8): count += 1

print(count)
