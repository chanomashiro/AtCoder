N = int(input())
A = list(map(int,input().split()))

m = A[0]
ans = 0
for i in range(1,N):
    ans += max(0, m - A[i])
    if m < A[i]:
        m = A[i]
print(ans)
