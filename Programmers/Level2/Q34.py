# 위장
def solution(clothes):
    c = dict()
    for clothe in clothes:
        name, cat = clothe
        if cat not in c:
            c[cat] = 1
        else:
            c[cat] += 1
    cnt = 1
    for val in c.values():
        cnt *= val + 1
    return cnt - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))