# 1
n = int(input())

num = 0
answer = 1

while True:
    num = num * 10 + 1
    num = num % n
    if num == 0:
        break
    answer += 1

print(answer)

# # 시간 초과 걸린 방법
# # 그래도 구현 측면에서는 조금 괜찮을 수도?
# answer = str(n)
#
# # 자릿수 숫자 생성
# n_dic = {}
# nn = n
# while len(n_dic) != 10:
#     if str(n)[-1] not in n_dic:
#         n_dic[str(n)[-1]] = n
#     else:
#         break
#     n += nn
#
# # 1로 된 숫자 생성
# idx = 0
# while len(answer) * '1' != str(answer):
#     for idx in range(len(answer)):
#         if answer[::-1][idx] != '1':
#             break
#     left_ans = answer[:len(answer) - idx]
#     left_ans_n = str(left_ans)[-1]
#     right_ans = '1' * idx
#     if left_ans_n == '0':
#         find_n = '1'
#     else:
#         find_n = str(11 - int(left_ans_n))
#     left_ans = str(int(left_ans) + n_dic[find_n])
#     answer = left_ans + right_ans
#
# print(len(answer))