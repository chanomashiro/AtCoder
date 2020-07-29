N,M = map(int,input().split())
A = list(map(int,input().split()))
soutokuhyou = sum(A)
A.sort(reverse=True)
if A[M-1] >= soutokuhyou * (1/(4*M)):
    print("Yes")
else:
    print("No")
