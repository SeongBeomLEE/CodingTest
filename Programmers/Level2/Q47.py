# 이진 변환 번복하기
def solution(s):
    ans = 0
    cnt = 0
    while len(s) != 1:
        s = list(s)
        total_len = len(s)
        cnt_1 = s.count('1')
        cnt_0 = total_len - cnt_1
        ans += cnt_0
        cnt += 1
        s = bin(cnt_1)[2:]
    answer = [cnt, ans]
    return answer
s = "110010101001"
print(solution(s))