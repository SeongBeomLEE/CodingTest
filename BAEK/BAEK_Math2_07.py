# 아이디어
# x, y는 각각 두쌍을 이룬다.
# 따라서 x, y 중 2개가 나오지 않은 숫자가
# 마지막 x, y 좌표이다.
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x_list = [x1, x2, x3]
y_list = [y1, y2, y3]
x4 = 0
y4 = 0
if x_list.count(min(x_list)) == 1:
    x4 = min(x_list)
if x_list.count(max(x_list)) == 1:
    x4 = max(x_list)
if y_list.count(min(y_list)) == 1:
    y4 = min(y_list)
if y_list.count(max(y_list)) == 1:
    y4 = max(y_list)
print(x4, y4)