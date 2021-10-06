# [1차] 뉴스 클러스터링
import string
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    lower_str = list(string.ascii_lowercase)

    str1_li = []
    for i in range(len(str1) - 1):
        _str1 = str1[i : i+2]
        if (_str1[0] in lower_str) and (_str1[1] in lower_str):
            str1_li.append(_str1)

    str2_li = []
    for i in range(len(str2) - 1):
        _str2 = str2[i : i+2]
        if (_str2[0] in lower_str) and (_str2[1] in lower_str):
            str2_li.append(_str2)

    # 교집합
    inter = []
    _str1_li = str1_li.copy()
    _str2_li = str2_li.copy()
    for str1 in str1_li:
        if str1 in _str2_li:
            inter.append(str1)
            _str1_li.remove(str1)
            _str2_li.remove(str1)

    # 합집합
    union = inter + _str1_li + _str2_li

    if len(union) == 0:
        answer = 65536
    else:
        answer = (len(inter) / len(union)) * 65536
    return int(answer)

# str1 = 'FRANCE'
# str2 = 'french'
# str1 = 'handshake'
# str1 = 'aa1+aa2'

str1 = 'aa1+aa2'
str2 = 'AAAA12'

print(solution(str1, str2))