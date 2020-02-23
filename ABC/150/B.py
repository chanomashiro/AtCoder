N = int(input())
S = str(input())
cnt = 0
for i in range(2,N):
    if S[i-2] == "A" and S[i-1] == "B" and S[i] == "C":
        cnt += 1
print(cnt)