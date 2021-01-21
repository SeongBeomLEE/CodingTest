def solution(x):
    ret = 0
    while x > 1:
        if ret > 500:
            ret = -1
            break
        elif x % 2 == 0:
            x = x/2
            ret += 1
        else:
            x = x*3 + 1
            ret += 1
    return ret
n = int(input())
print(solution(n))