N,K = map(int,input().split())
if N >= K:
    n = N % K
    print(min(abs(n-K),n))
else:
    print(min(abs(N-K),N))
