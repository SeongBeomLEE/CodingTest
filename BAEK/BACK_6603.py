# 로또
def get_answer(idx, answer):
    if len(answer) == 6: answer_li.append(answer)
    if len(answer) + (k - idx) >= 6:
        for i in range(idx + 1, k):
            get_answer(i, answer + [s[i]])

while True:
    test_case = input()
    if test_case == '0': break
    test_case = list(map(int, test_case.split()))
    k, s = test_case[0], test_case[1:]
    answer_li = []
    for i in range(0, k):
        get_answer(i, [s[i]])
    for answer in answer_li:
        print(' '.join(list(map(str, answer))))
    print()
