# 후위 표기식

strings = input()
p = ['+', '-', '*', '/', '(', ')']
stack = []
S = ''
for s in strings:
    if s not in p:
        S += s
    else:
        if stack:
            if s == ')':
                while stack and stack[-1] != '(':
                    S += stack.pop()
                stack.pop()
            elif s == '(': stack.append(s)
            elif s in ['+', '-']:
                while stack and stack[-1] != '(':
                    S += stack.pop()
                stack.append(s)
            elif s in ['*', '/']:
                while stack and stack[-1] in ['*', '/']:
                    S += stack.pop()
                stack.append(s)
        else: stack.append(s)

print(S + ''.join(list(reversed(stack))))