'''
우선 가능한 방법은
앞에서 부터 k개 까지의 방법임

'''
def solution(number, k):
    answer = ''
    stack = []
    total_len = len(number) - k
    for i in number:
        while stack and int(stack[-1]) < int(i) and k > 0:
            k -= 1
            stack.pop()
        stack.append(i)
    answer = ''.join(stack)[:len(stack) - k]
    return answer