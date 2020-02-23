N,K,M = map(int,input().split())
A = sum(list(map(int,input().split())))
M *= N

if (M - A) <= K:
    print(max(0, M - A))
else:
    print(-1)