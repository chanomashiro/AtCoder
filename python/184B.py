n,x = map(int,input().split())
s = list(input())
ans = x
for ss in s:
    if ss == "o":
        ans += 1
    else:
        ans = max(0, ans-1)
print(ans)