# 메뉴 리뉴얼
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        _answer = []
        for o in orders:
            if len(o) >= c:
                _answer += ["".join(sorted(i)) for i in combinations(o, c)]
        if _answer:
            _answer = sorted(list(Counter(_answer).items()), key = lambda x: x[1], reverse = True)
            max_num = _answer[0][1]
            if max_num > 1:
                for key, num in _answer:
                    if num == max_num:
                        answer.append(key)
                    else: break

    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
course = [2,3,5]
course = [2,3,4]
print(solution(orders, course))