N = int(input())
A = list(map(int,input().split()))
A.sort()

s = []
prev = 0
for a in A[::-1]:
    s.append(prev)
    prev += a
s = s[::-1]
ans = 0
for i, a in enumerate(A):
    ans += a * s[i]
    ans %= 10**9+7

print(ans)
