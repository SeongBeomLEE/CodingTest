# 다트 게임
def solution(dartResult):
    answer = []
    temp = ''
    dart_li = ['S', 'D', 'T', '*', '#']
    for idx, num in enumerate(dartResult):
        if num not in dart_li:
            temp += num
        else:
            if len(temp) != 0:
                answer.append(int(temp))
                temp = ''
            if num == dart_li[0]:
                n = answer.pop()
                n = n**1
                answer.append(n)
            elif num == dart_li[1]:
                n = answer.pop()
                n = n**2
                answer.append(n)
            elif num == dart_li[2]:
                n = answer.pop()
                n = n**3
                answer.append(n)
            elif num == dart_li[3]:
                idx = len(answer) - 1
                for _ in range(len(answer[-2:])):
                    answer[idx] = answer[idx] * 2
                    idx -= 1
            else:
                n = answer.pop()
                n = -1 * n
                answer.append(n)
    return sum(answer)
dartResult = "1D2S3T*"
print(solution(dartResult))