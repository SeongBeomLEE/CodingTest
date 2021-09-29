# 균형잡힌 세상
while True:
    line = input()
    if line == '.': break
    stack = []
    ans = True
    for s in line:
        if s == '(':
            stack.append(s)
        elif s == '[':
            stack.append(s)
        elif s == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    ans = False
                    break
            else:
                ans = False
                break
        elif s == ']':
            if stack:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    ans = False
                    break
            else:
                ans = False
                break
        elif s == '.': break
    if not stack and ans: print('yes')
    else: print('no')