# AC
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    pp = sys.stdin.readline().rstrip()
    n = int(input())
    n_li = sys.stdin.readline().rstrip()[1:-1].split(",")
    flag = 0
    rev = 0
    if n == 0 :
        n_li = []
    for p in pp:
        if p == 'R':
            rev += 1
        if p == 'D':
            if n_li:
                if rev % 2 == 0: del n_li[0]
                else: del n_li[-1]
            else:
                print('error')
                flag = 1
                break
    if flag != 1:
        if rev % 2 == 0: print('[' + ','.join(n_li) + ']')
        else: print('[' + ','.join(n_li[::-1])+ ']')