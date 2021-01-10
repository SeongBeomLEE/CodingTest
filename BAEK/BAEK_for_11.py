N, X = input().split()
A = input().split()
N = int(N)
X = int(X)
list = [i for i in A if int(i) < X]
print(" ".join(str(i) for i in list))