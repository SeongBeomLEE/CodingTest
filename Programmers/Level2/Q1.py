# 문자열 압축
def solution(s):
    answer = 1001
    max_split_size = len(s) // 2
    for split_size in range(1, max_split_size + 1):
        word = ''
        cnt = 1
        for size in range(0, len(s), split_size):
            now_word = s[size : size + split_size]
            next_word = s[size + split_size : size + 2 * split_size]
            if now_word == next_word:
                cnt += 1
            else:
                if cnt > 1:
                    word +=  str(cnt) + now_word
                    cnt = 1
                else: word += now_word
        answer = min(answer, len(word))

    if len(s) == 1:
        answer = 1

    return answer

s = "abcabcabcabcdededededede"
print(solution(s))
