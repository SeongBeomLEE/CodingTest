# k진수에서 소수 개수 구하기
def solution(n, k):
    answer = 0

    # 진수 변환
    change_n = ''
    while n > 0:
        n, m = divmod(n, k)
        change_n += str(m)
    change_n = change_n[::-1]

    # 소수 찾기
    num = ''
    for n in change_n:
        if n != '0':
            num += n
        else:
            if num and num != '1':
                num = int(num)
                temp = True
                for i in range(2, int(num ** 0.5 + 1)):
                    if num % i == 0:
                        temp = False
                        break
                if temp:
                    answer += 1
            num = ''

    if num and num != '1':
        num = int(num)
        temp = True
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                temp = False
                break
        if temp:
            answer += 1

    return answer

n = 110011
k = 10
print(solution(n, k))