N = int(input())
is_diff = []

cnt = 0
ans = "No"
for i in range(N):
    a,b = map(int,input().split())
    if a == b:
        cnt += 1
    else:
        cnt = 0
    if cnt == 3:
        ans = "Yes"
print(ans)

