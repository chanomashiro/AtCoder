N,K = map(int,input().split())
H = sorted(list(map(int,input().split())))
print(sum(H[:max(N-K,0)]))