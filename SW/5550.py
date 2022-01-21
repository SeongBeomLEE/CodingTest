# 나는 개구리로소이다

'''
본 문제의 핵심은 (1) c r o a k 순으로 무조건 등장하면서
(2) 최소한의 반복을 하는 개구리의 수를 구해야 한다.

(1)의 경우 dic 안의 문자 열의 수를 카운트 하면서
앞에 순서 보다 뒤에 순서가 먼저 발생하게 된다면 잘못된 문자열이다.

(2)의 경우 각 문자의 수를 세면서 c 가 등장했을 때(개구리 count의 시작)
각 문자 안에 모든 숫자가 1이상 이라면 -1을 해줌으로써
최소 한의 울음을 반복하는 개구리의 수를 보장할 수 있다.

'''

T = int(input())

for test_case in range(1, T + 1):
    frog_str = input()
    str_li = ['c', 'r', 'o', 'a', 'k']
    answer = -1
    frog_dic = {s : 0 for s in str_li}
    temp = False
    for s in frog_str:
        frog_dic[s] += 1

        # (1)
        for idx in range(1, len(str_li)):
            if frog_dic[str_li[idx - 1]] < frog_dic[str_li[idx]]:
                temp = True
        if temp: break

        # (2)
        if s == 'c' and 0 not in list(frog_dic.values()):
            for key in frog_dic.keys():
                frog_dic[key] -= 1

    if len(set(frog_dic.values())) == 1:
        answer = frog_dic['c']

    print(f'#{test_case} {answer}')

