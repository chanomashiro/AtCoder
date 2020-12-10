A,B = map(int,input().split())
cnt = 1
while True:
    if int(cnt * 0.08) == A and int(cnt * 0.1) == B:
        break
    cnt += 1
    if cnt > 1010:
        cnt = -1
        break
print(cnt)