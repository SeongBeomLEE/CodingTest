A = []
A_N = []
for i in range(10):
    N = int(input())
    A.append(N)
for i in A:
    N = i % 42
    A_N.append(N)

A_N = set(A_N)
print(len(A_N))