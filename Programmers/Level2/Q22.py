# 후보키
from itertools import combinations
def solution(relation):
    rows = len(relation)
    cols = [i for i in range(len(relation[0]))]
    answer_li = []
    _cols = []

    # 유일성
    for i in range(1, len(cols) + 1):
        _cols += list(combinations(cols, i))
    for _col in _cols:
        li = [''] * rows
        for _c in _col:
            for row in range(rows):
                li[row] += relation[row][_c]
        if len(set(li)) == rows:
            answer_li.append(set(_col))

    # 최소성
    result = []
    for answer in answer_li:
        if result:
            if answer not in result:
                temp = True
                for i in result:
                    if answer & i == i:
                        temp = False
                        break
                if temp:
                    result.append(answer)
        else:
            result.append(answer)
    return len(result)

relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

relation = [["a","1","aaa","c","ng"],
            ["a","1","bbb","e","g"],
            ["c","1","aaa","d","ng"],
            ["d","2","bbb","d","ng"]]
print(solution(relation))
