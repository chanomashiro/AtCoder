H, W = map(int,input().split())
mi = float("inf")
su = 0
for i in range(H):
    a = list(map(int,input().split()))
    mi = min(mi, min(a))
    su += sum(a)

ans = su - (mi * H * W)
print(ans)