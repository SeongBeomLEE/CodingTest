# 쿼드압축 후 개수 세기
def solution(arr):
    arr_li = [arr[:]]
    total_cnt_0 = 0
    total_cnt_1 = 0
    while arr_li:
        arr = arr_li.pop(0)
        cnt_0 = 0
        n = len(arr)
        for a in arr:
            for val in a:
                if val == 0:
                    cnt_0 += 1
        if cnt_0 == n * n: total_cnt_0 += 1
        elif cnt_0 == 0 : total_cnt_1 += 1
        else:
            n = n // 2

            arr_left = []
            arr_right = []
            for a in arr[:n][:]:
                arr_left.append(a[:n])
                arr_right.append(a[n:])
            arr_li.append(arr_left)
            arr_li.append(arr_right)

            arr_left = []
            arr_right = []
            for a in arr[n:][:]:
                arr_left.append(a[:n])
                arr_right.append(a[n:])
            arr_li.append(arr_left)
            arr_li.append(arr_right)

    answer = [total_cnt_0, total_cnt_1]
    return answer

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))