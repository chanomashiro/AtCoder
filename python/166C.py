N,M = map(int,input().split())
H = list(map(int,input().split()))
A = []
B = []
for i in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

H_state = [True for i in range(N)]

for i in range(M):
    if H[A[i]-1] >= H[B[i]-1]:
        H_state[B[i]-1] = False
    if H[B[i]-1] >= H[A[i]-1]:
        H_state[A[i]-1] = False
print(H_state.count(True))
