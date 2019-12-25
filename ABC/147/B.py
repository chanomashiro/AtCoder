S = str(input())
cnt = 0
for i in range(len(S)):
    if S[i] != S[-(i+1)]:
        cnt += 1
print(cnt//2)