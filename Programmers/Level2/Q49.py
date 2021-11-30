# n^2 배열 자르기
def solution(n, left, right):
    arr = []
    for i in range(left + 1, right + 2):
        q, r = divmod(i, n)
        if r == 0:
            arr += [n]
        else:
            if r <= (q + 1):
                arr += [q + 1]
            else:
                arr += [r]
    return arr

n = 4
left = 7
right = 14
print(solution(n, left, right))