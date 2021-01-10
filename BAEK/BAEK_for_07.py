N = int(input())
for i in range(1, N+1):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print("Case #{i}: {h}".format(i = i, h = A+B))