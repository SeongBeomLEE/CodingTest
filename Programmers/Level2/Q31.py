# 압축
import string
def solution(msg):
    LZW = {}
    ABC = string.ascii_uppercase
    for idx, val in enumerate(ABC):
        LZW[val] = idx + 1

    w_li = list(msg)
    c_li = list(msg[1:])
    cnt = 27
    while c_li:
        w = w_li.pop(0)
        c = c_li.pop(0)
        wc = w+c
        if wc not in LZW:
            w_li.append(w)
            LZW[wc] = cnt
            cnt += 1
        else:
            w_li.pop(0)
            w_li.insert(0, wc)

    w_li = w_li[1:] + w_li[:1]
    answer = [LZW[w] for w in w_li]
    return answer

msg = 'A'
print(solution(msg))