# 2개 이하로 다른 비트
def get_bit(num):
    ans = ''
    while num > 0:
        num, mod = divmod(num, 2)
        ans += str(mod)
    return ans[::-1]

def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            ans_li = []
            ans = list(get_bit(num))
            if '0' not in ans:
                ans = ['0'] + ans
            for idx in range(len(ans) - 1, -1, -1):
                if ans[idx] == '0':
                    ans_num = int('0b' + ''.join(ans[: idx] + ['10'] + ans[idx + 2:]), 2)
                    answer.append(ans_num)
                    break
    return answer
numbers = [2,7]
print(solution(numbers))