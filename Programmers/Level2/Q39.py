# 큰수만들기
def solution(number, k):
    stack = []
    for num in number:
        while stack and int(stack[-1]) < int(num) and k != 0 :
            k -= 1
            stack.pop()
        stack.append(num)
    answer = ''.join(stack)
    return answer[:-k] if k != 0 else answer
number = "1924"
k = 2
print(solution(number, k))
