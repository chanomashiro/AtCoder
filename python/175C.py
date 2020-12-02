X,K,D = map(int,input().split())
X = abs(X)

s = min(X//D, K)
X -= s * D

if (K - s) % 2 == 0:
    ans = X
else:
    ans = abs(X - D)
print(ans)
