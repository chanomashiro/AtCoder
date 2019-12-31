N = int(input())
A = list(map(int,input().split()))
nxt = 1
ans = 0
for a in A:
    if a == nxt:
        nxt += 1
    else:
        ans += 1
if ans == N:
    ans = -1
print(ans)