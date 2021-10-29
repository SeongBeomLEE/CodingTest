# 위장
from itertools import combinations
def solution(clothes):
    c = dict()
    for clothe in clothes:
        name, cat = clothe
        if cat not in c:
            c[cat] = [name]
        else:
            c[cat] += [name]
    key_li = list(c.keys())
    com_key_li = []
    for i in range(1, len(key_li) + 1):
        com_key_li += list(combinations(key_li, i))
    answer = 0
    for key in com_key_li:
        cnt = 1
        for k in key:
            cnt *= len(c[k])
        answer += cnt

    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))