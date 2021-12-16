from itertools import permutations
def solution(numbers):
    numbers = list(numbers)
    num_li = []
    for i in range(1, len(numbers) + 1):
        num_li += list(permutations(numbers, i))
    num_li = set([int(''.join(list(num))) for num in num_li])

    answer = 0
    for num in num_li:
        if num > 1:
            tmp = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    tmp = False
                    break
            if tmp:
                answer += 1

    return answer