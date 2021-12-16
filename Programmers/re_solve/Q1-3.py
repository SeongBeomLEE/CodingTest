from itertools import combinations
def solution(clothes):
    cloth_dic = {}
    for clo, cat in clothes:
        if cat not in cloth_dic:
            cloth_dic[cat] = 1
        else:
            cloth_dic[cat] += 1
    cat_cnt_li = list(cloth_dic.values())
    answer = 1
    for i in cat_cnt_li:
        answer *= (i + 1)
    return answer - 1