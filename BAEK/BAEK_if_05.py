H, M = input().split()
H = int(H)
M = int(M)
# 분
if (M - 45) < 0 :
    a = M - 45
    M = 60 + a
elif (M - 45) >= 0 :
    a = 1
    M = M - 45
# 시간
if (a < 0) & (0 < H <24):
    H = H - 1
elif (a >= 0) & (0 < H <24):
    H = H
elif (a < 0) & (H == 0):
    H = 24 - 1
print(H,M)