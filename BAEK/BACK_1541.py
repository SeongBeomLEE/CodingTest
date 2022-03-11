# 잃어버린 괄호
expression = input()

numbers = []
operators = []
num = ''
for val in expression:
    if val not in ['-', '+']:
        num += val
    else:
        numbers.append(int(num))
        num = ''
        operators.append(val)
if num:
    numbers.append(int(num))

val = 0
_numbers = []
_operators = []
for idx, number in enumerate(numbers):
    val += number
    if idx != len(operators) and operators[idx] == '-':
        _numbers.append(val)
        _operators.append(operators[idx])
        val = 0
if val != 0:
    _numbers.append(val)

answer = _numbers[0]
if _operators:
    for val in _numbers[1:]:
        answer -= val

print(answer)