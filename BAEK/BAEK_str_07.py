A, B = input().split()
A = int(A[::-1]) # 문자 뒤집기
B = int(B[::-1])
if A > B :
    print(A)
else:
    print(B)