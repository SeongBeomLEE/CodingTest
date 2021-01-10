N = int(input())
A = list(map(int,input().split()))

min = A[0]
max = A[0]

for i in range(N):
    if A[i] < min:
        min = A[i]
    if A[i] > max:
        max = A[i]

print(min, max)