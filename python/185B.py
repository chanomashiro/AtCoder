N,M,T = map(int,input().split())
N_max = N
current_time = 0
ans = True
for i in range(M):
    A,B = map(int,input().split())
    
    N -= (A - current_time)
    if N <= 0:
        ans = False
        break
    current_time = B

    N = min((N + (B - A)),N_max)
N -= T - current_time
if N <= 0:
    ans = False

if ans:
    print("Yes")
else:
    print("No")