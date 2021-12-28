def solution(n, m, k, data):
    '''
    결국 k + 1개의 수열이 반복된다고 볼 수 있다.
    왜? 제일 큰 수 k개 + 두번째로 큰 수 이기 때문에
    따라서 반복할 수열의 개수와 나머지 수의 개수를 찾는다.
    '''
    data.sort(reverse = True)
    f_num = data[0]
    s_num = data[1]

    ret_num = m // (k + 1)
    num = m % (k + 1)

    answer = (((f_num * k) + s_num) * ret_num) + (f_num * num)
    return answer


n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]
print(solution(n, m, k, data))