N = int(input())
S = str(input())
al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = ""
for s in S:
    ans += al[(al.index(s) + N) % 26]
print(ans)
