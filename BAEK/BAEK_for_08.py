N = int(input())
for i in range(1, N+1):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print("Case #{i}: {A} + {B} = {h}".format(i = i, A = A, B = B, h = A+B))