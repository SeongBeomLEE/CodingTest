# 두 배열의 원소 교체
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

N, K = 5, 3
A = [1,2,5,4,3]
B = [5,5,6,6,5]
A.sort() # 오름차순 정렬
B.sort(reverse=True) # 내림차순 정렬
for i in range(K):
    # 만약 A의 값이 B보다 작다면 서로의 원소를 교체
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: break

print(sum(A))


