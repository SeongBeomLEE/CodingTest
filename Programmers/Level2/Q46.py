# 모음 사전
def solution(word):
    word_dic = {}
    words = ['A', 'E', 'I', 'O', 'U']
    cnt = 1
    for w1 in words:
        word_dic[w1] = cnt
        cnt += 1
        for w2 in words:
            word_dic[w1 + w2] = cnt
            cnt += 1
            for w3 in words:
                word_dic[w1 + w2 + w3] = cnt
                cnt += 1
                for w4 in words:
                    word_dic[w1 + w2 + w3 + w4] = cnt
                    cnt += 1
                    for w5 in words:
                        word_dic[w1 + w2 + w3 + w4 + w5] = cnt
                        cnt += 1
    return word_dic[word]
word = "EIO"
print(solution(word))