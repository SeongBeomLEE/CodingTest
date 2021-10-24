# 괄호
def solve(strings):
    answer = []
    for string in strings:
        stack = []
        for s in string:
            if stack:
                if stack[-1] == '(':
                    if s == ')': stack.pop()
                    else: stack.append(s)
            else:stack.append(s)
        if stack: answer.append('NO')
        else: answer.append('YES')
    return answer

strings = []
for _ in range(int(input())):
    strings.append(input())

for answer in solve(strings):
    print(answer)