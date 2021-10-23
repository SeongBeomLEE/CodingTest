# 외벽점검
from itertools import permutations
def solution(n, weak, dist):
    answer_li = []
    weak_li = []
    for i in range(len(weak)):
        w = []
        front = weak[i:]
        back = weak[:i]
        for f in front:
            w.append(f)
        for b in back:
            w.append(b + n)
        weak_li.append(w)

    dist_li = []
    for i in range(1, len(dist) + 1):
        dist_li += list(map(list,permutations(dist, i)))

    temp = False
    for dist in dist_li:
        answer = len(dist)
        for weak in weak_li:
            _weak = weak.copy()
            _dist = dist.copy()
            w = _weak.pop(0)
            d = _dist.pop(0)
            start = w + d
            while _weak:
                if _weak[0] <= start:
                    _weak.pop(0)
                else:
                    if not _dist: break
                    w = _weak.pop(0)
                    d = _dist.pop(0)
                    start = w + d
            if not _weak:
                answer_li.append(answer)
                temp = True
                break
        if temp: break

    return min(answer_li) if temp else -1

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))