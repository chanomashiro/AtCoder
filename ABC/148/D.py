n = int(input())
A = list(map(int,input().split()))

i = 1
cnt = 0
for a in A:
    if a != i:
        cnt += 1
    else:
        i += 1
if cnt == n:
    print(-1)
else:
    print(cnt)

