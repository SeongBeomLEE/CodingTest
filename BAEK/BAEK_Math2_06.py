# 아이디어
# 총 길이는 4개
# 1. abs(y-h)
# 2. abs(y-0)
# 3. abs(x-w)
# 4. abs(x-0)
# 중 가장 작은 최솟값(min)
def solution(x, y, w, h):
    ret = [abs(y-h), abs(y-0), abs(x-w), abs(x-0)]
    return min(ret)

x, y, w, h = map(int, input().split())
print(solution(x, y, w, h))
