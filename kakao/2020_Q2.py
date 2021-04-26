# 수식 최대화
# 스택구조를 사용하는게 핵심
import re
import itertools

def cal(left, right, x):
    if x == "*": return left * right
    elif x == "+": return left + right
    else: return left - right


def solution(expression):
    # 숫자 배열
    numbers = re.split('[-*+]', expression)

    # 연산자 배열
    operators = re.findall('[-*+]', expression)

    # 연산자 우선 순위
    operators_set = list(set(operators))
    operators_com = list(itertools.permutations(operators_set, len(operators_set)))

    ret = 0
    for prior in operators_com:
        _numbers = numbers
        _operators = operators

        for i in prior:
            stact_num = []
            stack_op = []

            stact_num.append(_numbers[0])

            for j in range(len(_operators)):
                stact_num.append(_numbers[j + 1])
                stack_op.append(_operators[j])

                if stack_op[-1] == i:
                    right_num = stact_num.pop(-1)
                    left_num = stact_num.pop(-1)
                    op = stack_op.pop(-1)

                    stact_num.append(cal(int(left_num), int(right_num), op))

            _numbers = stact_num
            _operators = stack_op

        assert(len(_numbers) == 1)
        assert(len(_operators) == 0)
        ret = max(ret, abs(_numbers[0]))

    return ret

expression = "100-200*300-500+20"
print(solution(expression))

