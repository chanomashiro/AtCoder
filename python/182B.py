N = int(input())
A = list(map(int,input().split()))
ans = None
gcd = 0
for i in range(2,1001):
    cnt = 0
    for a in A:
        if a % i == 0:
            cnt += 1
    if gcd < cnt:
        ans = i
        gcd = cnt
print(ans)