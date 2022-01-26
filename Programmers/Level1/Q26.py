# [1차] 다트 게임
def solution(dartResult):
    str_li = ['S', 'D', 'T', '*', '#']
    answer = []
    num = ''
    for d in dartResult:
        if d not in str_li:
            num += d
        else:
            if d == str_li[0]:
                num = int(num)
                num = num**1
                answer.append(num)
                num = ''
            elif d == str_li[1]:
                num = int(num)
                num = num ** 2
                answer.append(num)
                num = ''
            elif d == str_li[2]:
                num = int(num)
                num = num ** 3
                answer.append(num)
                num = ''
            elif d == str_li[3]:
                last_idx = len(answer) - 1
                answer[last_idx] = answer[last_idx] * 2
                if last_idx > 0:
                    last_idx2 = last_idx - 1
                    answer[last_idx2] = answer[last_idx2] * 2
            else:
                answer[-1] = answer[-1] * -1

    return sum(answer)
dartResult = '1S2D*3T'
print(solution(dartResult))

