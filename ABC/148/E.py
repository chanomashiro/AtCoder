N = int(input())

if N % 2 != 0:
    print(0)
else:
    ans = 0
    N //= 10
    ans += N
    while N != 0:
        N //= 5
        ans += N
    print(ans)