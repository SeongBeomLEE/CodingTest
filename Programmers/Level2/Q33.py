# N진수 게임
def solution(n, t, m, p):
    answer = ''
    mod2ABC = {10 : 'A', 11 : 'B', 12 : 'C', 13:'D', 14 : 'E', 15 : 'F'}
    for num in range(t * m * p):
        rev = ''
        while num > 0:
            num, mod = divmod(num, n)
            if mod >= 10:
                mod = mod2ABC[mod]
            rev += str(mod)
        if not rev: rev = '0'
        answer += rev[::-1]
        if t * m * p <= len(answer):break
    ret = ''
    cnt = 1
    for idx in range(p - 1, t * m * p, m):
        ret += answer[idx]
        if cnt == t: break
        cnt += 1
    return ret

n = 16
t = 16
m = 2
p = 2
print(solution(n, t, m, p))