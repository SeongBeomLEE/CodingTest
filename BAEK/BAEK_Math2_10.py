# 점이 접하는 점의 개수가 곧 정답
# 두원이 일치할 때 : -1
# r == 0 and r1 == r2
# 두원이 한점에서 접할때 (외접과 내접) : 1
# r== r1 + r2 or r+(r1과 r2중 작은 값) == (r1과 r2중 큰 값)
# 두원이 겹치지 않을 때 : 0
# 가장작은 2개의 R < 가장 큰 R
# 두원이 두점에서 겹칠 때 : 2
for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    r = ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)
    r_list = [r1, r2, r]
    max_r = max(r_list)
    r_list.remove(max_r)
    if (r==0) & (r1 == r2): print(-1)
    elif (r == r1 + r2) | (max_r == sum(r_list)): print(1)
    elif max_r > sum(r_list): print(0)
    else: print(2)