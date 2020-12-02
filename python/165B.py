X = int(input())

a = 100
cnt = 0
while True:
    a += a // 100
    cnt += 1
    if a >= X:
        break
print(cnt)