N = int(input())
S = input()
cnt = 0
prev = None
for s in S:
    if s != prev:
        cnt += 1
    prev = s
print(cnt)