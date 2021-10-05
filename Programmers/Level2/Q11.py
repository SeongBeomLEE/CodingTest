# 괄호변환
def solution(p):
    if p:
        left_count = 0
        right_count = 0
        u = ''
        for _p in p:
            u += _p
            if _p == '(':
                left_count += 1
            else:
                right_count += 1
            if left_count == right_count:
                break
        v = p[len(u):]
        stack = []
        for _u in u:
            if stack:
                if stack[-1] == '(' and _u == ')':
                    stack.pop()
                else:
                    stack.append(_u)
            else:
                stack.append(_u)
        if stack:
            answer = '(' + solution(v) + ')'
            for _u in u[1:-1]:
                if _u == '(':
                    answer += ')'
                else:
                    answer += '('
            return answer
        else:
            return u + solution(v)
    else: return p

p = "(()())()"
p = ")("
p = "()))((()"
print(solution(p))