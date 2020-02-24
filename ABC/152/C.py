N = int(input())
P = list(map(int,input().split()))
mi = float("inf")
cnt = 0

for p in P:
    mi = min(mi, p)
    if p <= mi:
        cnt += 1

print(cnt)