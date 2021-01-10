x = int(input())
y = int(input())
# 1사분면
if (x > 0) & (y > 0):
    print(1)
# 2사분면
if (x < 0) & (y > 0):
    print(2)
# 3사분면
if (x < 0) & (y < 0):
    print(3)
# 4사분면
if (x > 0) & (y < 0):
    print(4)