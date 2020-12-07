N,A,B = map(int,input().split())
cnt = 0
cnt += (N//(A+B)) * A
cnt += min(N%(A+B),A)
print(cnt)